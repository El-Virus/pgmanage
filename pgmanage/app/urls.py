from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

base_urlpatterns = [

    # path('social-auth/', include('social_django.urls', namespace="social")),
    #LOGIN
    path('', views.login.check_session, name='check_session'),
    path('pgmanage_login/', views.login.index, name='login'),
    path('logout/', views.login.logout, name='logout'),
    path('check_session_message/', views.login.check_session_message, name='check_session_message'),
    path('sign_in/', views.login.sign_in, name='sign_in'),

    path('upload/', views.plugins.upload_view, name='sign_in'),

    path('long_polling/', views.polling.long_polling, name='long_polling'),
    path('create_request/', views.polling.create_request, name='create_request'),
    path('clear_client/', views.polling.clear_client, name='clear_client'),
    path('client_keep_alive/', views.polling.client_keep_alive, name='client_keep_alive'),

    #CONNECTIONS
    path('get_connections/', views.connections.get_connections, name='get_connections'),
    path('save_connection/', views.connections.save_connection, name='save_connection'),
    path('delete_connection/', views.connections.delete_connection, name='delete_connection'),
    path('test_connection/', views.connections.test_connection, name='test_connection'),

    path('get_groups/', views.connections.get_groups, name='get_groups'),
    path('save_group/', views.connections.save_group, name='save_group'),
    path('delete_group/', views.connections.delete_group, name='delete_group'),

    path('get_existing_tabs/', views.connections.get_existing_tabs, name='get_existing_tabs'),

    #USERS
    path('get_users/', views.users.get_users, name='get_users'),
    path('remove_user/', views.users.remove_user, name='remove_user'),
    path('save_users/', views.users.save_users, name='save_users'),

    #WORKSPACE
    path('workspace/', views.workspace.index, name='workspace'),
    path('renew_password/', views.workspace.renew_password, name='renew_password'),
    path('master_password/', views.workspace.master_password, name='master_password'),
    path('reset_master_password/', views.workspace.reset_master_password, name='reset_master_password'),
    path('draw_graph/', views.workspace.draw_graph, name='draw_graph'),
    path('get_table_columns/', views.workspace.get_table_columns, name='get_table_columns'),
    path('refresh_monitoring/', views.workspace.refresh_monitoring, name='refresh_monitoring'),
    path('delete_plugin/', views.plugins.delete_plugin, name='delete_plugin'),
    path('get_database_meta/', views.workspace.get_database_meta, name='get_database_meta'),

    #SETINGS
    path('settings/', views.workspace.SettingsView.as_view(), name="settings"),
    path('save-user-password/', views.workspace.save_user_password, name="save-user-password"),

    #COMMANDS HISTORY
    path('get_commands_history/', views.commands_history.get_commands_history, name="get_commands_history"),
    path('clear_commands_history/', views.commands_history.clear_commands_history, name="clear_commands_history"),

    #HOOKS
    path('get_plugins/', views.plugins.get_plugins, name='get_plugins'),
    path('list_plugins/', views.plugins.list_plugins, name='list_plugins'),
    path('reload_plugins/', views.plugins.reload_plugins, name='reload_plugins'),
    path('exec_plugin_function/', views.plugins.exec_plugin_function, name='exec_plugin_function'),

    #TREE_SNIPPETS
    path('get_node_children/', views.tree_snippets.get_node_children, name='get_node_children'),
    path('get_snippet_text/', views.tree_snippets.get_snippet_text, name='get_snippet_text'),
    path('new_node_snippet/', views.tree_snippets.new_node_snippet, name='new_node_snippet'),
    path('delete_node_snippet/', views.tree_snippets.delete_node_snippet, name='delete_node_snippet'),
    path('save_snippet_text/', views.tree_snippets.save_snippet_text, name='save_snippet_text'),
    path('rename_node_snippet/', views.tree_snippets.rename_node_snippet, name='rename_node_snippet'),
    path('get_all_snippets/', views.tree_snippets.get_all_snippets, name='get_all_snippets'),

    #TREE_POSTGRESQL
    path('get_tree_info_postgresql/', views.tree_postgresql.get_tree_info, name='get_tree_info'),
    path('get_tables_postgresql/', views.tree_postgresql.get_tables, name='get_tables'),
    path('get_schemas_postgresql/', views.tree_postgresql.get_schemas, name='get_schemas'),
    path('get_columns_postgresql/', views.tree_postgresql.get_columns, name='get_columns'),
    path('get_pk_postgresql/', views.tree_postgresql.get_pk, name='get_pk'),
    path('get_pk_columns_postgresql/', views.tree_postgresql.get_pk_columns, name='get_pk_columns'),
    path('get_fks_postgresql/', views.tree_postgresql.get_fks, name='get_fks'),
    path('get_fks_columns_postgresql/', views.tree_postgresql.get_fks_columns, name='get_fks_columns'),
    path('get_uniques_postgresql/', views.tree_postgresql.get_uniques, name='get_uniques'),
    path('get_uniques_columns_postgresql/', views.tree_postgresql.get_uniques_columns, name='get_uniques_columns'),
    path('get_indexes_postgresql/', views.tree_postgresql.get_indexes, name='get_indexes'),
    path('get_indexes_columns_postgresql/', views.tree_postgresql.get_indexes_columns, name='get_indexes_columns'),
    path('get_checks_postgresql/', views.tree_postgresql.get_checks, name='get_checks'),
    path('get_excludes_postgresql/', views.tree_postgresql.get_excludes, name='get_excludes'),
    path('get_rules_postgresql/', views.tree_postgresql.get_rules, name='get_rules'),
    path('get_rule_definition_postgresql/', views.tree_postgresql.get_rule_definition, name='get_rule_definition'),
    path('get_triggers_postgresql/', views.tree_postgresql.get_triggers, name='get_triggers'),
    path('get_eventtriggers_postgresql/', views.tree_postgresql.get_eventtriggers, name='get_eventtriggers'),
    path('get_inheriteds_postgresql/', views.tree_postgresql.get_inheriteds, name='get_inheriteds'),
    path('get_inheriteds_parents_postgresql/', views.tree_postgresql.get_inheriteds_parents, name='get_inheriteds_parents'),
    path('get_inheriteds_children_postgresql/', views.tree_postgresql.get_inheriteds_children, name='get_inheriteds_children'),
    path('get_partitions_postgresql/', views.tree_postgresql.get_partitions, name='get_partitions'),
    path('get_partitions_parents_postgresql/', views.tree_postgresql.get_partitions_parents, name='get_partitions_parents'),
    path('get_partitions_children_postgresql/', views.tree_postgresql.get_partitions_children, name='get_partitions_children'),
    path('get_statistics_postgresql/', views.tree_postgresql.get_statistics, name='get_statistics'),
    path('get_statistics_columns_postgresql/', views.tree_postgresql.get_statistics_columns, name='get_statistics_columns'),
    path('get_functions_postgresql/', views.tree_postgresql.get_functions, name='get_functions'),
    path('get_function_fields_postgresql/', views.tree_postgresql.get_function_fields, name='get_function_fields'),
    path('get_function_definition_postgresql/', views.tree_postgresql.get_function_definition, name='get_function_definition'),
    path('get_function_debug_postgresql/', views.tree_postgresql.get_function_debug, name='get_function_debug'),
    path('get_procedures_postgresql/', views.tree_postgresql.get_procedures, name='get_procedures'),
    path('get_procedure_fields_postgresql/', views.tree_postgresql.get_procedure_fields, name='get_procedure_fields'),
    path('get_procedure_definition_postgresql/', views.tree_postgresql.get_procedure_definition, name='get_procedure_definition'),
    path('get_procedure_debug_postgresql/', views.tree_postgresql.get_procedure_debug, name='get_procedure_debug'),
    # new endpoint used by schema builder
    path('get_table_definition_postgresql/', views.tree_postgresql.get_table_definition, name='get_table_definition'),
    path('get_triggerfunctions_postgresql/', views.tree_postgresql.get_triggerfunctions, name='get_triggerfunctions'),
    path('get_triggerfunction_definition_postgresql/', views.tree_postgresql.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    path('get_eventtriggerfunctions_postgresql/', views.tree_postgresql.get_eventtriggerfunctions, name='get_eventtriggerfunctions'),
    path('get_eventtriggerfunction_definition_postgresql/', views.tree_postgresql.get_eventtriggerfunction_definition, name='get_eventtriggerfunction_definition'),
    path('get_aggregates_postgresql/', views.tree_postgresql.get_aggregates, name='get_aggregates'),
    path('get_sequences_postgresql/', views.tree_postgresql.get_sequences, name='get_sequences'),
    path('get_views_postgresql/', views.tree_postgresql.get_views, name='get_views'),
    path('get_views_columns_postgresql/', views.tree_postgresql.get_views_columns, name='get_views_columns'),
    path('get_view_definition_postgresql/', views.tree_postgresql.get_view_definition, name='get_view_definition'),
    path('get_mviews_postgresql/', views.tree_postgresql.get_mviews, name='get_mviews'),
    path('get_mviews_columns_postgresql/', views.tree_postgresql.get_mviews_columns, name='get_mviews_columns'),
    path('get_mview_definition_postgresql/', views.tree_postgresql.get_mview_definition, name='get_mview_definition'),
    path('get_databases_postgresql/', views.tree_postgresql.get_databases, name='get_databases'),
    path('get_tablespaces_postgresql/', views.tree_postgresql.get_tablespaces, name='get_tablespaces'),
    path('get_roles_postgresql/', views.tree_postgresql.get_roles, name='get_roles'),
    path('get_extensions_postgresql/', views.tree_postgresql.get_extensions, name='get_extensions'),
    path('get_extension_details/', views.tree_postgresql.get_extension_details, name='get_extension_details'),
    path('save_postgresql_extension/', views.tree_postgresql.save_extension, name="save_postgresql_extension"),
    path('get_available_extensions_postgresql/', views.tree_postgresql.get_available_extensions, name='get_available_extensions'),
    path('get_physicalreplicationslots_postgresql/', views.tree_postgresql.get_physicalreplicationslots, name='get_physicalreplicationslots'),
    path('get_logicalreplicationslots_postgresql/', views.tree_postgresql.get_logicalreplicationslots, name='get_logicalreplicationslots'),
    path('get_publications_postgresql/', views.tree_postgresql.get_publications, name='get_publications'),
    path('get_subscriptions_postgresql/', views.tree_postgresql.get_subscriptions, name='get_subscriptions'),
    path('get_publication_tables_postgresql/', views.tree_postgresql.get_publication_tables, name='get_publication_tables'),
    path('get_subscription_tables_postgresql/', views.tree_postgresql.get_subscription_tables, name='get_subscription_tables'),
    path('get_foreign_data_wrappers_postgresql/', views.tree_postgresql.get_foreign_data_wrappers, name='get_foreign_data_wrappers'),
    path('get_foreign_servers_postgresql/', views.tree_postgresql.get_foreign_servers, name='get_foreign_servers'),
    path('get_user_mappings_postgresql/', views.tree_postgresql.get_user_mappings, name='get_user_mappings'),
    path('get_foreign_tables_postgresql/', views.tree_postgresql.get_foreign_tables, name='get_foreign_tables'),
    path('get_foreign_columns_postgresql/', views.tree_postgresql.get_foreign_columns, name='get_foreign_columns'),
    path('get_types_postgresql/', views.tree_postgresql.get_types, name='get_types'),
    path('get_domains_postgresql/', views.tree_postgresql.get_domains, name='get_domains'),
    path('kill_backend_postgresql/', views.tree_postgresql.kill_backend, name='kill_backend'),
    path('get_properties_postgresql/', views.tree_postgresql.get_properties, name='get_properties'),
    path('get_database_objects_postgresql/', views.tree_postgresql.get_database_objects, name='get_database_objects'),
    path('template_select_postgresql/', views.tree_postgresql.template_select, name='template_select'),
    path('template_insert_postgresql/', views.tree_postgresql.template_insert, name='template_insert'),
    path('template_update_postgresql/', views.tree_postgresql.template_update, name='template_update'),
    path('template_select_function_postgresql/', views.tree_postgresql.template_select_function, name='template_select_function'),
    path('template_call_procedure_postgresql/', views.tree_postgresql.template_call_procedure, name='template_call_procedure'),
    path('change_active_database/', views.workspace.change_active_database, name='change_active_database'),
    path('get_postgresql_version/', views.tree_postgresql.get_version, name='get_version'),
    path('change_role_password_postgresql/', views.tree_postgresql.change_role_password, name='change_role_password'),
    path('get_object_description_postgresql/', views.tree_postgresql.get_object_description, name='get_object_description'),\

    #PG_CRON
    path('get_pgcron_jobs/', views.pgextras.get_pgcron_jobs, name='get_pgcron_jobs'),
    path('get_pgcron_job_details/', views.pgextras.get_pgcron_job_details, name='get_pgcron_job_details'),
    path('get_pgcron_job_logs/', views.pgextras.get_pgcron_job_logs, name='get_pgcron_job_logs'),
    path('delete_pgcron_job_logs/', views.pgextras.delete_pgcron_job_logs, name='delete_pgcron_job_logs'),
    path('save_pgcron_job/', views.pgextras.save_pgcron_job, name='save_pgcron_job'),
    path('delete_pgcron_job/', views.pgextras.delete_pgcron_job, name='delete_pgcron_job'),

    #TREE_ORACLE
    path('get_tree_info_oracle/', views.tree_oracle.get_tree_info, name='get_tree_info'),
    path('get_tables_oracle/', views.tree_oracle.get_tables, name='get_tables'),
    path('get_columns_oracle/', views.tree_oracle.get_columns, name='get_columns'),
    path('get_pk_oracle/', views.tree_oracle.get_pk, name='get_pk'),
    path('get_pk_columns_oracle/', views.tree_oracle.get_pk_columns, name='get_pk_columns'),
    path('get_fks_oracle/', views.tree_oracle.get_fks, name='get_fks'),
    path('get_fks_columns_oracle/', views.tree_oracle.get_fks_columns, name='get_fks_columns'),
    path('get_uniques_oracle/', views.tree_oracle.get_uniques, name='get_uniques'),
    path('get_uniques_columns_oracle/', views.tree_oracle.get_uniques_columns, name='get_uniques_columns'),
    path('get_indexes_oracle/', views.tree_oracle.get_indexes, name='get_indexes'),
    path('get_indexes_columns_oracle/', views.tree_oracle.get_indexes_columns, name='get_indexes_columns'),
    #re_path(r'^get_triggers_oracle/', views.tree_oracle.get_triggers, name='get_triggers'),
    #re_path(r'^get_partitions_oracle/', views.tree_oracle.get_partitions, name='get_partitions'),
    path('get_functions_oracle/', views.tree_oracle.get_functions, name='get_functions'),
    path('get_function_fields_oracle/', views.tree_oracle.get_function_fields, name='get_function_fields'),
    path('get_function_definition_oracle/', views.tree_oracle.get_function_definition, name='get_function_definition'),
    path('get_procedures_oracle/', views.tree_oracle.get_procedures, name='get_procedures'),
    path('get_procedure_fields_oracle/', views.tree_oracle.get_procedure_fields, name='get_procedure_fields'),
    path('get_procedure_definition_oracle/', views.tree_oracle.get_procedure_definition, name='get_procedure_definition'),
    #re_path(r'^get_function_debug_oracle/', views.tree_oracle.get_function_debug, name='get_function_debug'),
    #re_path(r'^get_triggerfunctions_oracle/', views.tree_oracle.get_triggerfunctions, name='get_triggerfunctions'),
    #re_path(r'^get_triggerfunction_definition_oracle/', views.tree_oracle.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    path('get_sequences_oracle/', views.tree_oracle.get_sequences, name='get_sequences'),
    path('get_views_oracle/', views.tree_oracle.get_views, name='get_views'),
    path('get_views_columns_oracle/', views.tree_oracle.get_views_columns, name='get_views_columns'),
    path('get_view_definition_oracle/', views.tree_oracle.get_view_definition, name='get_view_definition'),
    #re_path(r'^get_mviews_oracle/', views.tree_oracle.get_mviews, name='get_mviews'),
    #re_path(r'^get_mviews_columns_oracle/', views.tree_oracle.get_mviews_columns, name='get_mviews_columns'),
    #re_path(r'^get_mview_definition_oracle/', views.tree_oracle.get_mview_definition, name='get_mview_definition'),
    path('get_tablespaces_oracle/', views.tree_oracle.get_tablespaces, name='get_tablespaces'),
    path('get_roles_oracle/', views.tree_oracle.get_roles, name='get_roles'),
    path('kill_backend_oracle/', views.tree_oracle.kill_backend, name='kill_backend'),
    path('get_properties_oracle/', views.tree_oracle.get_properties, name='get_properties'),
    path('template_select_oracle/', views.tree_oracle.template_select, name='template_select'),
    path('template_insert_oracle/', views.tree_oracle.template_insert, name='template_insert'),
    path('template_update_oracle/', views.tree_oracle.template_update, name='template_update'),

    #TREE_MYSQL
    path('get_tree_info_mysql/', views.tree_mysql.get_tree_info, name='get_tree_info'),
    path('get_tables_mysql/', views.tree_mysql.get_tables, name='get_tables'),
    path('get_columns_mysql/', views.tree_mysql.get_columns, name='get_columns'),
    path('get_pk_mysql/', views.tree_mysql.get_pk, name='get_pk'),
    path('get_pk_columns_mysql/', views.tree_mysql.get_pk_columns, name='get_pk_columns'),
    path('get_fks_mysql/', views.tree_mysql.get_fks, name='get_fks'),
    path('get_fks_columns_mysql/', views.tree_mysql.get_fks_columns, name='get_fks_columns'),
    path('get_uniques_mysql/', views.tree_mysql.get_uniques, name='get_uniques'),
    path('get_uniques_columns_mysql/', views.tree_mysql.get_uniques_columns, name='get_uniques_columns'),
    path('get_indexes_mysql/', views.tree_mysql.get_indexes, name='get_indexes'),
    path('get_indexes_columns_mysql/', views.tree_mysql.get_indexes_columns, name='get_indexes_columns'),
    #re_path(r'^get_triggers_mysql/', views.tree_mysql.get_triggers, name='get_triggers'),
    #re_path(r'^get_partitions_mysql/', views.tree_mysql.get_partitions, name='get_partitions'),
    path('get_functions_mysql/', views.tree_mysql.get_functions, name='get_functions'),
    path('get_function_fields_mysql/', views.tree_mysql.get_function_fields, name='get_function_fields'),
    path('get_function_definition_mysql/', views.tree_mysql.get_function_definition, name='get_function_definition'),
    path('get_procedures_mysql/', views.tree_mysql.get_procedures, name='get_procedures'),
    path('get_procedure_fields_mysql/', views.tree_mysql.get_procedure_fields, name='get_procedure_fields'),
    path('get_procedure_definition_mysql/', views.tree_mysql.get_procedure_definition, name='get_procedure_definition'),
    #re_path(r'^get_function_debug_mysql/', views.tree_mysql.get_function_debug, name='get_function_debug'),
    #re_path(r'^get_triggerfunctions_mysql/', views.tree_mysql.get_triggerfunctions, name='get_triggerfunctions'),
    #re_path(r'^get_triggerfunction_definition_mysql/', views.tree_mysql.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    #re_path(r'^get_sequences_mysql/', views.tree_mysql.get_sequences, name='get_sequences'),
    path('get_views_mysql/', views.tree_mysql.get_views, name='get_views'),
    path('get_views_columns_mysql/', views.tree_mysql.get_views_columns, name='get_views_columns'),
    path('get_view_definition_mysql/', views.tree_mysql.get_view_definition, name='get_view_definition'),
    path('get_databases_mysql/', views.tree_mysql.get_databases, name='get_databases'),
    path('get_roles_mysql/', views.tree_mysql.get_roles, name='get_roles'),
    path('kill_backend_mysql/', views.tree_mysql.kill_backend, name='kill_backend'),
    path('get_properties_mysql/', views.tree_mysql.get_properties, name='get_properties'),
    path('template_select_mysql/', views.tree_mysql.template_select, name='template_select'),
    path('template_insert_mysql/', views.tree_mysql.template_insert, name='template_insert'),
    path('template_update_mysql/', views.tree_mysql.template_update, name='template_update'),
    path('get_table_definition_mysql/', views.tree_mysql.get_table_definition, name='get_table_definition'),

    #TREE_MARIADB
    path('get_tree_info_mariadb/', views.tree_mariadb.get_tree_info, name='get_tree_info'),
    path('get_tables_mariadb/', views.tree_mariadb.get_tables, name='get_tables'),
    path('get_columns_mariadb/', views.tree_mariadb.get_columns, name='get_columns'),
    path('get_pk_mariadb/', views.tree_mariadb.get_pk, name='get_pk'),
    path('get_pk_columns_mariadb/', views.tree_mariadb.get_pk_columns, name='get_pk_columns'),
    path('get_fks_mariadb/', views.tree_mariadb.get_fks, name='get_fks'),
    path('get_fks_columns_mariadb/', views.tree_mariadb.get_fks_columns, name='get_fks_columns'),
    path('get_uniques_mariadb/', views.tree_mariadb.get_uniques, name='get_uniques'),
    path('get_uniques_columns_mariadb/', views.tree_mariadb.get_uniques_columns, name='get_uniques_columns'),
    path('get_indexes_mariadb/', views.tree_mariadb.get_indexes, name='get_indexes'),
    path('get_indexes_columns_mariadb/', views.tree_mariadb.get_indexes_columns, name='get_indexes_columns'),
    #re_path(r'^get_triggers_mariadb/', views.tree_mariadb.get_triggers, name='get_triggers'),
    #re_path(r'^get_partitions_mariadb/', views.tree_mariadb.get_partitions, name='get_partitions'),
    path('get_functions_mariadb/', views.tree_mariadb.get_functions, name='get_functions'),
    path('get_function_fields_mariadb/', views.tree_mariadb.get_function_fields, name='get_function_fields'),
    path('get_function_definition_mariadb/', views.tree_mariadb.get_function_definition, name='get_function_definition'),
    path('get_procedures_mariadb/', views.tree_mariadb.get_procedures, name='get_procedures'),
    path('get_procedure_fields_mariadb/', views.tree_mariadb.get_procedure_fields, name='get_procedure_fields'),
    path('get_procedure_definition_mariadb/', views.tree_mariadb.get_procedure_definition, name='get_procedure_definition'),
    #re_path(r'^get_function_debug_mariadb/', views.tree_mariadb.get_function_debug, name='get_function_debug'),
    #re_path(r'^get_triggerfunctions_mariadb/', views.tree_mariadb.get_triggerfunctions, name='get_triggerfunctions'),
    #re_path(r'^get_triggerfunction_definition_mariadb/', views.tree_mariadb.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    path('get_sequences_mariadb/', views.tree_mariadb.get_sequences, name='get_sequences'),
    path('get_views_mariadb/', views.tree_mariadb.get_views, name='get_views'),
    path('get_views_columns_mariadb/', views.tree_mariadb.get_views_columns, name='get_views_columns'),
    path('get_view_definition_mariadb/', views.tree_mariadb.get_view_definition, name='get_view_definition'),
    path('get_databases_mariadb/', views.tree_mariadb.get_databases, name='get_databases'),
    path('get_roles_mariadb/', views.tree_mariadb.get_roles, name='get_roles'),
    path('kill_backend_mariadb/', views.tree_mariadb.kill_backend, name='kill_backend'),
    path('get_properties_mariadb/', views.tree_mariadb.get_properties, name='get_properties'),
    path('template_select_mariadb/', views.tree_mariadb.template_select, name='template_select'),
    path('template_insert_mariadb/', views.tree_mariadb.template_insert, name='template_insert'),
    path('template_update_mariadb/', views.tree_mariadb.template_update, name='template_update'),

    #TREE_SQLITE
    path('get_tree_info_sqlite/', views.tree_sqlite.get_tree_info, name='get_tree_info'),
    path('get_tables_sqlite/', views.tree_sqlite.get_tables, name='get_tables'),
    path('get_columns_sqlite/', views.tree_sqlite.get_columns, name='get_columns'),
    path('get_pk_sqlite/', views.tree_sqlite.get_pk, name='get_pk'),
    path('get_pk_columns_sqlite/', views.tree_sqlite.get_pk_columns, name='get_pk_columns'),
    path('get_fks_sqlite/', views.tree_sqlite.get_fks, name='get_fks'),
    path('get_fks_columns_sqlite/', views.tree_sqlite.get_fks_columns, name='get_fks_columns'),
    path('get_uniques_sqlite/', views.tree_sqlite.get_uniques, name='get_uniques'),
    path('get_uniques_columns_sqlite/', views.tree_sqlite.get_uniques_columns, name='get_uniques_columns'),
    path('get_indexes_sqlite/', views.tree_sqlite.get_indexes, name='get_indexes'),
    path('get_indexes_columns_sqlite/', views.tree_sqlite.get_indexes_columns, name='get_indexes_columns'),
    path('get_triggers_sqlite/', views.tree_sqlite.get_triggers, name='get_triggers'),
    path('get_views_sqlite/', views.tree_sqlite.get_views, name='get_views'),
    path('get_views_columns_sqlite/', views.tree_sqlite.get_views_columns, name='get_views_columns'),
    path('get_view_definition_sqlite/', views.tree_sqlite.get_view_definition, name='get_view_definition'),
    path('get_properties_sqlite/', views.tree_sqlite.get_properties, name='get_properties'),
    path('template_select_sqlite/', views.tree_sqlite.template_select, name='template_select'),
    path('template_insert_sqlite/', views.tree_sqlite.template_insert, name='template_insert'),
    path('template_update_sqlite/', views.tree_sqlite.template_update, name='template_update'),
    path('get_table_definition_sqlite/', views.tree_sqlite.get_table_definition, name="get_table_definition_sqlite"),

    #MONITORING SYSTEM
    path("monitoring-widgets", views.monitoring_dashboard.monitoring_widgets, name="monitoring-widgets"),
    path("monitoring-widgets/list", views.monitoring_dashboard.monitoring_widgets_list, name="monitoring-widgets-list"),
    path("monitoring-widgets/test", views.monitoring_dashboard.test_monitoring_widget, name="test-monitoring-widget"),
    path("monitoring-widgets/create", views.monitoring_dashboard.create_dashboard_monitoring_widget, name="create-dashboard-widget"),
    path("monitoring-widgets/<int:widget_id>", views.monitoring_dashboard.widget_detail, name="dashboard-widget-detail"),
    path("monitoring-widgets/<int:widget_id>/template", views.monitoring_dashboard.widget_template, name="widget-template"),
    path("monitoring-widgets/<int:widget_saved_id>/refresh", views.monitoring_dashboard.refresh_monitoring_widget, name="refresh-monitoring-widget"),
    path("monitoring-widgets/user-created", views.monitoring_dashboard.create_widget, name="create-custom-widget"),
    path("monitoring-widgets/user-created/<int:widget_id>", views.monitoring_dashboard.user_created_widget_detail, name="widget-detail"),

    # Configuration
    path('configuration/<int:config_id>/', views.configuration.delete_config, name="delete_configuration"),
    path('configuration/', views.configuration.get_configuration, name='get_configuration'),
    path('configuration/categories/', views.configuration.get_configuration_categories, name='get_configuration_categories'),
    path('save_configuration/', views.configuration.save_configuration, name='save_configuration'),
    path('get_configuration_history/', views.configuration.get_configuration_history, name='get_configuration_history'),
    path('configuration/status/', views.configuration.get_status, name="settings_status"),

    # Backup and Restore
    path('backup/', views.backup.create_backup, name='create_backup'),
    path('backup/preview_command/', views.backup.preview_command, name='backup_preview_command'),
    path('restore/', views.restore.create_restore, name='create_restore'),
    path('restore/preview_command/', views.restore.preview_command, name='restore_preview_command'),

    # Background jobs
    path('bgprocess/', views.bgjob.index, name='job_list'),
    path('bgprocess/<int:job_id>/<int:out>/<int:err>/', views.bgjob.details, name='job_details'),
    path('bgprocess/stop/<int:job_id>/', views.bgjob.stop_job, name='stop_job'),
    path('bgprocess/delete/<int:job_id>/', views.bgjob.delete_job, name='delete_job'),
    # File Management
    path('file_manager/get_directory/', views.file_manager.get_directory, name="get_directory"),
    path('file_manager/create/', views.file_manager.create, name="create_file_or_directory"),
    path('file_manager/rename/', views.file_manager.rename, name="rename_file_or_directory"),
    path('file_manager/delete/', views.file_manager.delete, name='delete_file_or_directory'),

    path('validate_binary_path/', views.workspace.validate_binary_path, name='validate_binary_path'),

    path('log/', views.logging.log_message, name="log_message")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.PATH == '':
    v_url = ''
else:
    v_url = settings.PATH[1:] + '/'

urlpatterns = [# if you wish to maintain the un-prefixed URL's too
    path(v_url, include(base_urlpatterns)),
    #re_path(r'^subfolder/', include(base_urlpatterns))
]
