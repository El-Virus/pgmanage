import { useSnippetsStore } from "./snippets";
import { useSettingsStore } from "./settings";
import { useTabsStore } from "./tabs";
import { useConnectionsStore } from "./connections";
import { useUtilityJobsStore } from "./utility_jobs";
import { createPinia, setActivePinia } from "pinia";

const pinia = createPinia();
setActivePinia(pinia);

const snippetsStore = useSnippetsStore();

const settingsStore = useSettingsStore();

const tabsStore = useTabsStore();

const connectionsStore = useConnectionsStore();

const utilityJobStore = useUtilityJobsStore();

export {
  snippetsStore,
  settingsStore,
  tabsStore,
  connectionsStore,
  utilityJobStore,
};
