import { useSnippetsStore } from "./snippets";
import { useSettingsStore } from "./settings";
import { useTabsStore } from "./tabs";
import { useConnectionsStore } from "./connections";
import { useUtilityJobsStore } from "./utility_jobs";
import { useDbMetadataStore } from "./db_metadata";
import { useMessageModalStore } from "./message_modal";
import { createPinia, setActivePinia } from "pinia";

const pinia = createPinia();
setActivePinia(pinia);

const snippetsStore = useSnippetsStore();

const settingsStore = useSettingsStore();

const tabsStore = useTabsStore();

const connectionsStore = useConnectionsStore();

const dbMetadataStore = useDbMetadataStore();

const utilityJobStore = useUtilityJobsStore();

const messageModalStore = useMessageModalStore();

export {
  snippetsStore,
  settingsStore,
  tabsStore,
  connectionsStore,
  utilityJobStore,
  dbMetadataStore,
  messageModalStore,
};
