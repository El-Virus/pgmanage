import { settingsModalInit } from './settings_modal.js'
import { connectionsModalInit, conn_app} from './connections_modal.js'
import { connectionsStore } from './stores/connections.js'
import { passwordModalsInit, showNewMasterPassPrompt, showMasterPassPrompt } from './passwords.js'
import { format } from 'sql-formatter'
import ContextMenu from '@imengyu/vue3-context-menu'
import { createRequest } from './long_polling'
import { queryRequestCodes } from './constants'
import { checkDebugStatus } from './debug'
import { startLoading } from './ajax_control'
import axios from 'axios'
import { showAlert, showConfirm } from './notification_control'
import { emitter } from './emitter'
import { startTutorial } from './tutorial'
import { tabsStore } from './stores/stores_initializer.js'


let v_start_height;
/// <summary>
/// Startup function.
/// </summary>
$(function () {
  settingsModalInit()

  // Creating omnis.
  v_omnis.root = document.getElementById('app');
  v_omnis.div = document.createElement('div');
  v_omnis.div.setAttribute('id', 'omnis');
  v_omnis.div.classList.add('omnis');
  v_omnis.div.style.top = v_omnis.root.getBoundingClientRect().height - 45 + 'px';
  v_omnis.div.style.left = v_omnis.root.getBoundingClientRect().width - 45 + 'px';
  v_omnis.div.style['z-index'] = '99999999';
  v_omnis.div.style.opacity = 0
  v_omnis.div.innerHTML = v_omnis.template;
  document.body.appendChild(v_omnis.div);
  v_omnis.div.addEventListener('click',function(){
    startTutorial('getting_started');
  });

  passwordModalsInit()
  // Ask for master password
  if (master_key === 'new') {
    showNewMasterPassPrompt(`Please set your master password. It will be used to secure your connection credentials.`);
  } else if (master_key == 'False'){
    showMasterPassPrompt(`Please provide your master password to unlock your connection credentials for this session.`);
  } else {
    conn_app.mount("#connections-modal-wrap");
    v_omnis.div.style.opacity = 1
  }


  // Loads or Updates all tooltips.
  $('[data-toggle="tooltip"]').tooltip({animation:true});

  connectionsModalInit()
});


/// <summary>
/// Check if there are troublesome tabs
/// </summary>
/// <param name="p_cancel_function">Ok function.</param>
/// <param name="p_ok_function">Cancel function.</param>
function checkBeforeChangeDatabase(p_cancel_function, p_ok_function) {

  for (const tab of tabsStore.selectedPrimaryTab.metaData.secondaryTabs) {
    if(["edit", "alter", "debug", "monitoring_dashboard", "data_mining"].includes(tab.metaData.mode)) {
      showAlert('Before changing connection please close any tab that belongs to the following types: <br/><br/><b>Edit Data<br/><br/>Alter Table<br/><br/>Function Debugging<br/><br/>Monitoring Dashboard<br/><br/>Advanced Object Search');
      if (p_cancel_function!=null) {
        p_cancel_function();
      }
      return false;
    }
  }

	if (p_ok_function!=null) {
    p_ok_function();
  }
  return true;
}


/// <summary>
/// Rename tab.
/// </summary>
function renameTab(p_tab) {

	showConfirm('<input id="tab_name"/ class="form-control" value="' + p_tab.tag.tab_title_span.innerHTML + '" style="width: 100%;">',
    function() {
			renameTabConfirm(p_tab,document.getElementById('tab_name').value);
    },
    null,
    function() {
      var v_input = document.getElementById('tab_name');
      v_input.focus();
      v_input.selectionStart = 0;
      v_input.selectionEnd = 10000;
    }
  );
	var v_input = document.getElementById('tab_name');
	v_input.onkeydown = function() {
		if (event.keyCode == 13) {
      document.getElementById('modal_message_ok').click();
    }
		else if (event.keyCode == 27) {
      document.getElementById('modal_message_cancel').click();
    }
	}

}


/// <summary>
/// Renames tab.
/// </summary>
function renameTabConfirm(p_tab, p_name) {

	p_tab.tag.tab_title_span.innerHTML = p_name;

}


function resizeWindow(){
	refreshHeights(true);
}


var resizeTimeout;
$(window).resize(function() {
	clearTimeout(resizeTimeout);
	resizeTimeout = setTimeout(resizeWindow, 200);
});


/// <summary>
/// Refresh divs sizes and components of the currently selected tab
/// </summary>
function refreshHeights(p_all) {
  setTimeout(function(){

    if (v_connections_data && v_connections_data.v_active) {
      v_connections_data.ht.render();
    }

    if (v_connTabControl.selectedTab.tag.mode=='monitor_all') {
      v_connTabControl.selectedTab.tag.tabControlDiv.style.height = window.innerHeight - $(v_connTabControl.selectedTab.tag.tabControlDiv).offset().top - (1.5)*v_font_size + 'px';
    }

    else if (v_connTabControl.selectedTab.tag.mode=='outer_terminal') {
      v_connTabControl.selectedTab.tag.div_console.style.height = window.innerHeight - $(v_connTabControl.selectedTab.tag.div_console).offset().top - (0.2)*v_font_size + 'px';
      v_connTabControl.selectedTab.tag.fitAddon.fit();
    }

    //If inner tab exists
    if (v_connTabControl.selectedTab.tag.tabControl != null && v_connTabControl.selectedTab.tag.tabControl.selectedTab) {
      var v_tab_tag = v_connTabControl.selectedTab.tag.tabControl.selectedTab.tag;

      if (v_tab_tag.mode=='debug' || v_tab_tag.mode=='edit' || v_tab_tag.mode=='graph' || v_tab_tag.mode=='monitor_grid' || v_tab_tag.mode=='monitor_unit' || v_tab_tag.mode=='website' || v_tab_tag.mode=='website_outer') {
          v_tab_tag.resize();
      }
      else if (v_tab_tag.mode === 'console') {
        emitter.emit(`${v_tab_tag.tab_id}_resize`)
      }
      // else if (v_tab_tag.mode=='query_history') {
      //   v_tab_tag.div_result.style.height = window.innerHeight - $(v_tab_tag.div_result).offset().top - (1.75)*v_font_size + 'px';
      //   if (v_tab_tag.ht!=null)
      //   v_tab_tag.ht.render();
      // }
      else if (v_tab_tag.mode=='alter') {
        if (v_tab_tag.alterTableObject.window=='columns') {
          var v_height = window.innerHeight - $(v_tab_tag.htDivColumns).offset().top - 45;
          v_tab_tag.htDivColumns.style.height = v_height + 'px';
          if (v_tab_tag.alterTableObject.htColumns!=null) {
            v_tab_tag.alterTableObject.htColumns.render();
          }
        }
        else if (v_tab_tag.alterTableObject.window=='constraints') {
          var v_height = window.innerHeight - $(v_tab_tag.htDivConstraints).offset().top - 45;
          v_tab_tag.htDivConstraints.style.height = v_height + 'px';
          if (v_tab_tag.alterTableObject.htConstraints!=null) {
            v_tab_tag.alterTableObject.htConstraints.render();
          }
        }
        else {
          var v_height = window.innerHeight - $(v_tab_tag.htDivIndexes).offset().top - 45;
          v_tab_tag.htDivIndexes.style.height = v_height + 'px';
          if (v_tab_tag.alterTableObject.htIndexes!=null) {
            v_tab_tag.alterTableObject.htIndexes.render();
          }
        }
      }
      else if(v_tab_tag.mode == 'data_mining') {
        if(v_tab_tag.currQueryTab == 'data') {
          v_tab_tag.div_result.style.height = window.innerHeight - $(v_tab_tag.div_result).offset().top - (1.25)*v_font_size + 'px';
        }
      }
    }

    // Updating position of omnis.
    if (v_omnis) {
      if (v_omnis.omnis_ui_assistant) {
        v_omnis.omnis_ui_assistant.goToStep(v_omnis.omnis_ui_assistant.stepSelected);
      }
      else if (v_omnis.div) {
        v_omnis.div.style.top = v_omnis.root.getBoundingClientRect().height - 45 + 'px';
        v_omnis.div.style.left = v_omnis.root.getBoundingClientRect().width - 45 + 'px';
      }
    }

  },351);
}


function showMenuNewTabOuter(e) {
  function getConnectionInfo(conn) {
    let conn_name = "";
    let tooltip_name = "";
    let name = "";
    if (conn.public) {
      conn_name += '<i class="fas fa-users mr-3" style="color:#c57dd2;"></i>';
    }
    if (conn.alias) {
      name = conn.alias;
      conn_name += `(${conn.alias})`;
      tooltip_name += `<h5 class="my-1">${conn.alias}</h5>`;
    }
    if (conn.conn_string) {
      conn_name += ` ${conn.conn_string}`;
      tooltip_name += `<div class="mb-1">${conn.conn_string}</div>`;
    } else {
      if (conn.details1) {
        conn_name += conn.details1;
        tooltip_name += `<div class="mb-1">${conn.details1}</div>`;
      }
      if (conn.details2) {
        conn_name += ` - ${conn.details2}`;
        tooltip_name += `<div class="mb-1">${conn.details2}</div>`;
      }
    }
    return [conn, conn_name, tooltip_name, name];
  }

  function createConnectionGroup(group) {
    const group_connections = connectionsStore.connections
      .filter((conn) => group.conn_list.includes(conn.id))
      .map((conn) => {
        const [_, conn_name, tooltip_name, name] = getConnectionInfo(conn);
        let icon =
          conn.technology == "terminal"
            ? "fa-terminal"
            : `node node-${conn.technology}`;
        let onClick;
        if (conn.technology == "terminal") {
          onClick = () => {
            emitter.emit(`${tabsStore.id}_create_terminal_tab`, {index: conn.id, alias: conn.alias, details: conn.details1})
          };
        } else {
          onClick = () => {
            emitter.emit(`${tabsStore.id}_create_conn_tab`, {
              index: conn.id,
              createInitialTabs: true,
              name: name,
              tooltipName: tooltip_name})
          };
        }
        return {
          label: conn_name,
          icon: `fas cm-all ${icon}`,
          onClick: onClick,
        };
      });

    return {
      label: group.name,
      icon: "fas cm-all fa-plug",
      children: group_connections,
    };
  }
  // Opening connections management when there are no configured connections.
  if (
    !connectionsStore.connections ||
    connectionsStore.connections.length === 0
  ) {
    $("#connections-modal").modal({
      show: true,
    });
  } else {
    let items = [];

    // Building connection list
    if (connectionsStore.connections.length > 0) {
      // No custom groups, render all connections in the same list
      if (!connectionsStore.groups.length) {
        const connectionsList = createConnectionGroup({
          name: "Connections",
          conn_list: connectionsStore.connections.map((conn) => conn.id),
        });

        items.push(connectionsList);
      }
      //Render connections split in groups
      else {
        const group_list = [
          createConnectionGroup({
            name: "All Connections",
            conn_list: connectionsStore.connections.map((conn) => conn.id),
          }),
          ...connectionsStore.groups.map(createConnectionGroup),
        ];

        items.push({
          label: "Connections",
          icon: "fas cm-all fa-plug",
          children: group_list,
        });
      }
    }

    if (connectionsStore.remote_terminals.length > 0) {
      const submenu_terminal_list = connectionsStore.remote_terminals.map(
        (term) => {
          const { id, alias, details1 } = term;
          let term_name = alias ? `(${alias})` : "";
          if (details1) {
            term_name += details1;
          }
          return {
            label: term_name,
            icon: "fas cm-all fa-terminal",
            onClick: () => {
              emitter.emit(`${tabsStore.id}_create_terminal_tab`, {index: id, alias: alias, details: details1})
            },
          };
        }
      );

      items.push({
        label: "SSH Consoles",
        icon: "fas cm-all fa-terminal",
        children: submenu_terminal_list,
      });
    }

    if (items.length > 0) {
      items.unshift({
        label: "Manage Connections",
        icon: "fas cm-all fa-gears",
        onClick: () => {
          $("#connections-modal").modal({
            show: true,
          });
        },
      });

      ContextMenu.showContextMenu({
        theme: "pgmanage",
        x: e.x,
        y: e.y,
        zIndex: 1000,
        minWidth: 230,
        items: items,
      });
    } else {
      startLoading();
      setTimeout(function () {
        emitter.emit(`${tabsStore.id}_create_conn_tab`)
      }, 0);
    }
  }
}

export {
  refreshHeights,
  renameTab,
  checkBeforeChangeDatabase,
  renameTabConfirm,
  showMenuNewTabOuter
};