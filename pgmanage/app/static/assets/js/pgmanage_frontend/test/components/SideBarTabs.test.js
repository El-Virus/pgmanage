import {
  describe,
  test,
  vi,
  expect,
  beforeEach,
  afterEach,
  beforeAll,
} from "vitest";
import { mount, enableAutoUnmount } from "@vue/test-utils";

vi.hoisted(() => {
  vi.stubGlobal("v_csrf_cookie_name", "test_cookie");
})

import SideBarTabs from "../../src/components/SideBarTabs.vue";
import "bootstrap";
import { nextTick } from "vue";
import { emitter } from "../../src/emitter";
import { useTabsStore } from "../../src/stores/tabs";
import { useConnectionsStore } from "../../src/stores/connections";

vi.mock("@/workspace.js", () => {
  const showMenuNewTabOuter = vi.fn();

  return { showMenuNewTabOuter };
});

vi.mock("@/header_actions.js", () => {
  const showConfigUser = vi.fn;
  return { showConfigUser };
});

vi.mock("xterm", () => {
  const Terminal = vi.fn();
  return { Terminal };
});

const connectionMock = {
  id: 1,
  alias: "TestConnection",
  technology: "postgresql",
};
vi.stubGlobal("app_base_path", "test_folder");

describe("SideBarTabs.vue", () => {
  enableAutoUnmount(afterEach);
  let tabsStore, connectionsStore;

  beforeAll(() => {
    connectionsStore = useConnectionsStore();
    connectionsStore.$patch({ connections: [connectionMock] });
  });

  beforeEach(() => {
    tabsStore = useTabsStore();
  });

  afterEach(() => {
    tabsStore.$reset();
  });
  test("renders a component", async () => {
    let wrapper = mount(SideBarTabs, {
      shallow: true,
    });

    expect(wrapper.html()).toContain("omnidb__tab-menu--container--primary");
    await nextTick();

    expect(wrapper.html()).toContain("Snippets");
    expect(wrapper.html()).toContain("Connections");
    expect(wrapper.html()).toContain("Welcome");
  });
});
