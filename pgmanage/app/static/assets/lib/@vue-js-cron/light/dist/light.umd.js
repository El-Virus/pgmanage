(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports, require('@vue-js-cron/core'), require('vue')) :
  typeof define === 'function' && define.amd ? define(['exports', '@vue-js-cron/core', 'vue'], factory) :
  (global = typeof globalThis !== 'undefined' ? globalThis : global || self, factory(global.light = {}, global.CronCore, global.vue));
})(this, (function (exports, CronCore, vue) { 'use strict';

  function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e : { 'default': e }; }

  var CronCore__default = /*#__PURE__*/_interopDefaultLegacy(CronCore);

  var script$1 = {
    inheritAttrs: false,
    components: {
      RenderlessSelect: CronCore.RenderlessSelect
    },
    name: 'CustomSelect',
    props: {},
    emits: ['update:model-value'],
    data () {
      return {
        menu: false
      }
    },
    methods: {
      menuEvtListener (evt) {
        this.menu = false;
        document.removeEventListener('click', this.menuEvtListener);
      },
      toggleMenu () {
        this.menu = !this.menu;

        if (this.menu) {
          setTimeout(() => {
            document.addEventListener('click', this.menuEvtListener);
          }, 1);
        } else {
          document.removeEventListener('click', this.menuEvtListener);
        }
      }
    }
  };

  const _hoisted_1$1 = { class: "vcron-select-container" };
  const _hoisted_2$1 = {
    key: 0,
    class: "vcron-select-list"
  };
  const _hoisted_3$1 = ["onClick"];
  const _hoisted_4 = { key: 0 };

  function render$1(_ctx, _cache, $props, $setup, $data, $options) {
    const _component_renderless_select = vue.resolveComponent("renderless-select");

    return (vue.openBlock(), vue.createBlock(_component_renderless_select, vue.mergeProps(_ctx.$attrs, {
      "onUpdate:modelValue": _cache[1] || (_cache[1] = $event => (_ctx.$emit('update:model-value', $event)))
    }), {
      default: vue.withCtx(({ selectedStr, itemRows, select, isSelected, multiple }) => [
        vue.createElementVNode("div", _hoisted_1$1, [
          vue.createElementVNode("span", {
            class: "vcron-select-input",
            onClick: _cache[0] || (_cache[0] = (...args) => ($options.toggleMenu && $options.toggleMenu(...args)))
          }, vue.toDisplayString(selectedStr), 1 /* TEXT */),
          ($data.menu)
            ? (vue.openBlock(), vue.createElementBlock("div", _hoisted_2$1, [
                (vue.openBlock(true), vue.createElementBlock(vue.Fragment, null, vue.renderList(itemRows, (row, i) => {
                  return (vue.openBlock(), vue.createElementBlock("div", {
                    class: "vcron-select-row",
                    key: i
                  }, [
                    (vue.openBlock(true), vue.createElementBlock(vue.Fragment, null, vue.renderList(row, (item, j) => {
                      return (vue.openBlock(), vue.createElementBlock("div", {
                        key: i+'-'+j,
                        class: vue.normalizeClass(["vcron-select-col", {'vcron-select-selected': isSelected(item)}]),
                        onClick: [
                          $event => (select(item)),
                          vue.withModifiers($event => (multiple ? () => {} : $options.toggleMenu()), ["stop"])
                        ]
                      }, [
                        item
                          ? (vue.openBlock(), vue.createElementBlock("div", _hoisted_4, vue.toDisplayString(item.text), 1 /* TEXT */))
                          : vue.createCommentVNode("v-if", true)
                      ], 10 /* CLASS, PROPS */, _hoisted_3$1))
                    }), 128 /* KEYED_FRAGMENT */))
                  ]))
                }), 128 /* KEYED_FRAGMENT */))
              ]))
            : vue.createCommentVNode("v-if", true)
        ])
      ]),
      _: 1 /* STABLE */
    }, 16 /* FULL_PROPS */))
  }

  script$1.render = render$1;
  script$1.__file = "src/components/CustomSelect.vue";

  var script = {
    name: 'VueCronEditor',
    components: {
      CronCore: CronCore__default["default"].component,
      CustomSelect: script$1
    },
    props: {
      cols: {
        type: Object,
        default: () => {
          return {
            minute: 5,
            hour: 4,
            day: 4
          }
        }
      }
    },
    emits: ['update:model-value', 'error']
  };

  const _hoisted_1 = { class: "vcron-editor" };
  const _hoisted_2 = { class: "vcron-l-spacer" };
  const _hoisted_3 = { class: "vcron-l-spacer" };

  function render(_ctx, _cache, $props, $setup, $data, $options) {
    const _component_custom_select = vue.resolveComponent("custom-select");
    const _component_CronCore = vue.resolveComponent("CronCore");

    return (vue.openBlock(), vue.createBlock(_component_CronCore, vue.mergeProps(_ctx.$attrs, {
      "onUpdate:modelValue": _cache[0] || (_cache[0] = $event => (_ctx.$emit('update:model-value', $event))),
      onError: _cache[1] || (_cache[1] = $event => (_ctx.$emit('error', $event)))
    }), {
      default: vue.withCtx(({fields, period}) => [
        vue.createElementVNode("span", _hoisted_1, [
          vue.createElementVNode("span", null, vue.toDisplayString(period.prefix), 1 /* TEXT */),
          vue.createElementVNode("div", _hoisted_2, [
            vue.createVNode(_component_custom_select, vue.mergeProps(period.attrs, vue.toHandlers(period.events), {
              items: period.items,
              "item-value": "id",
              cols: $props.cols['period'] || 1
            }), null, 16 /* FULL_PROPS */, ["items", "cols"])
          ]),
          vue.createElementVNode("span", null, vue.toDisplayString(period.suffix), 1 /* TEXT */),
          (vue.openBlock(true), vue.createElementBlock(vue.Fragment, null, vue.renderList(fields, (f) => {
            return (vue.openBlock(), vue.createElementBlock(vue.Fragment, {
              key: f.id
            }, [
              vue.createElementVNode("span", null, vue.toDisplayString(f.prefix), 1 /* TEXT */),
              vue.createElementVNode("div", _hoisted_3, [
                vue.createVNode(_component_custom_select, vue.mergeProps(f.attrs, vue.toHandlers(f.events), {
                  items: f.items,
                  cols: $props.cols[f.id] || 1,
                  selection: f.selectedStr,
                  multiple: ""
                }), null, 16 /* FULL_PROPS */, ["items", "cols", "selection"])
              ]),
              vue.createElementVNode("span", null, vue.toDisplayString(f.suffix), 1 /* TEXT */)
            ], 64 /* STABLE_FRAGMENT */))
          }), 128 /* KEYED_FRAGMENT */))
        ])
      ]),
      _: 1 /* STABLE */
    }, 16 /* FULL_PROPS */))
  }

  script.render = render;
  script.__file = "src/CronEditor.vue";

  // Import vue component

  // Declare install function executed by Vue.use()
  function install (Vue) {
    if (install.installed) return
    install.installed = true;
    Vue.component('CronLight', script);
  }

  // Create module definition for Vue.use()
  const plugin = {
    install,
    component: script,
    util: CronCore__default["default"].util
  };

  exports.CronLight = script;
  exports.CronLightPlugin = plugin;
  exports["default"] = plugin;
  exports.install = install;

  Object.defineProperty(exports, '__esModule', { value: true });

}));
