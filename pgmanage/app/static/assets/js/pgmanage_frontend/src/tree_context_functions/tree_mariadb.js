import { tabSQLTemplate } from "./tree_postgresql";
import { showToast } from "../notification_control";
import { emitter } from "../emitter";
import { tabsStore } from "../stores/stores_initializer";
import axios from "axios";

function TemplateSelectMariadb(schema, table) {
  axios
    .post("/template_select_mariadb/", {
      database_index:
        tabsStore.selectedPrimaryTab.metaData.selectedDatabaseIndex,
      tab_id: tabsStore.selectedPrimaryTab.id,
      table: table,
      schema: schema,
    })
    .then((resp) => {
      let tab_name = `${schema}.${table}`;
      tabsStore.createQueryTab(tab_name, null, null, resp.data.template);

      setTimeout(() => {
        emitter.emit(
          `${tabsStore.selectedPrimaryTab.metaData.selectedTab.id}_run_query`
        );
      }, 200);
    })
    .catch((error) => {
      showToast("error", error.response.data.data);
    });
}

function TemplateInsertMariadb(schema, table) {
  axios
    .post("/template_insert_mariadb/", {
      database_index:
        tabsStore.selectedPrimaryTab.metaData.selectedDatabaseIndex,
      tab_id: tabsStore.selectedPrimaryTab.id,
      table: table,
      schema: schema,
    })
    .then((resp) => {
      tabSQLTemplate(`Insert ${schema}.${table}`, resp.data.template);
    })
    .catch((error) => {
      showToast("error", error.response.data.data);
    });
}

function TemplateUpdateMariadb(schema, table) {
  axios
    .post("/template_update_mariadb/", {
      database_index:
        tabsStore.selectedPrimaryTab.metaData.selectedDatabaseIndex,
      tab_id: tabsStore.selectedPrimaryTab.id,
      table: table,
      schema: schema,
    })
    .then((resp) => {
      tabSQLTemplate(`Update ${schema}.${table}`, resp.data.template);
    })
    .catch((error) => {
      showToast("error", error.response.data.data);
    });
}

export { TemplateSelectMariadb, TemplateInsertMariadb, TemplateUpdateMariadb };
