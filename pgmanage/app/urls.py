#from django.conf.urls import url
from django.urls import include, re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

base_urlpatterns = [

    # path('social-auth/', include('social_django.urls', namespace="social")),

    re_path(r'^upload/$', views.plugins.upload_view, name='sign_in'),

    re_path(r'^long_polling/$', views.polling.long_polling, name='long_polling'),
    re_path(r'^create_request/$', views.polling.create_request, name='create_request'),
    re_path(r'^clear_client/$', views.polling.clear_client, name='clear_client'),
    re_path(r'^client_keep_alive/$', views.polling.client_keep_alive, name='client_keep_alive'),

    #LOGIN
    re_path(r'^$', views.login.check_session, name='check_session'),
    re_path(r'^pgmanage_login/', views.login.index, name='login'),
    re_path(r'^logout/', views.login.logout, name='logout'),
    re_path(r'^check_session_message/$', views.login.check_session_message, name='check_session_message'),
    re_path(r'^sign_in/$', views.login.sign_in, name='sign_in'),

    #CONNECTIONS
    re_path(r'^get_connections/$', views.connections.get_connections, name='get_connections'),
    re_path(r'^save_connection/$', views.connections.save_connection, name='save_connection'),
    re_path(r'^delete_connection/$', views.connections.delete_connection, name='delete_connection'),
    re_path(r'^test_connection/$', views.connections.test_connection, name='test_connection'),

    re_path(r'^get_groups/$', views.connections.get_groups, name='get_groups'),
    re_path(r'^save_group/$', views.connections.save_group, name='save_group'),
    re_path(r'^delete_group/$', views.connections.delete_group, name='delete_group'),

    re_path(r'^get_existing_tabs/$', views.connections.get_existing_tabs, name='get_existing_tabs'),

    #USERS
    re_path(r'^get_users/$', views.users.get_users, name='get_users'),
    re_path(r'^new_user/$', views.users.new_user, name='new_user'),
    re_path(r'^remove_user/$', views.users.remove_user, name='remove_user'),
    re_path(r'^save_users/$', views.users.save_users, name='save_users'),

    #WORKSPACE
    re_path(r'^workspace/', views.workspace.index, name='workspace'),
    re_path(r'^save_config_user/', views.workspace.save_config_user, name='save_config_user'),
    re_path(r'^shortcuts/', views.workspace.shortcuts, name='shortcuts'),
    re_path(r'^renew_password/', views.workspace.renew_password, name='renew_password'),
    re_path(r'^master_password/', views.workspace.master_password, name='master_password'),
    re_path(r'^reset_master_password/', views.workspace.reset_master_password, name='reset_master_password'),
    re_path(r'^draw_graph/', views.workspace.draw_graph, name='draw_graph'),
    re_path(r'^start_edit_data/', views.workspace.start_edit_data, name='start_edit_data'),
    re_path(r'^get_table_columns/', views.workspace.get_table_columns, name='get_table_columns'),
    re_path(r'^get_completions_table/', views.workspace.get_completions_table, name='get_completions_table'),
    re_path(r'^refresh_monitoring/', views.workspace.refresh_monitoring, name='refresh_monitoring'),
    re_path(r'^get_autocomplete_results/', views.workspace.get_autocomplete_results, name='get_autocomplete_results'),
    re_path(r'^delete_plugin/', views.plugins.delete_plugin, name='delete_plugin'),

    #COMMANDS HISTORY
    re_path(r'^get_command_list/', views.commands_history.get_command_list, name='get_command_list'),
    re_path(r'^clear_command_list/', views.commands_history.clear_command_list, name='clear_command_list'),
    re_path(r'^get_console_history/', views.commands_history.get_console_history, name='get_console_history'),
    re_path(r'^clear_console_list/', views.commands_history.clear_console_list, name='clear_console_list'),

    #HOOKS
    re_path(r'^get_plugins/', views.plugins.get_plugins, name='get_plugins'),
    re_path(r'^list_plugins/', views.plugins.list_plugins, name='list_plugins'),
    re_path(r'^reload_plugins/', views.plugins.reload_plugins, name='reload_plugins'),
    re_path(r'^exec_plugin_function/', views.plugins.exec_plugin_function, name='exec_plugin_function'),

    #TREE_SNIPPETS
    re_path(r'^get_node_children/', views.tree_snippets.get_node_children, name='get_node_children'),
    re_path(r'^get_snippet_text/', views.tree_snippets.get_snippet_text, name='get_snippet_text'),
    re_path(r'^new_node_snippet/', views.tree_snippets.new_node_snippet, name='new_node_snippet'),
    re_path(r'^delete_node_snippet/', views.tree_snippets.delete_node_snippet, name='delete_node_snippet'),
    re_path(r'^save_snippet_text/', views.tree_snippets.save_snippet_text, name='save_snippet_text'),
    re_path(r'^rename_node_snippet/', views.tree_snippets.rename_node_snippet, name='rename_node_snippet'),
    re_path(r'^get_all_snippets/', views.tree_snippets.get_all_snippets, name='get_all_snippets'),

    #TREE_POSTGRESQL
    re_path(r'^get_tree_info_postgresql/', views.tree_postgresql.get_tree_info, name='get_tree_info'),
    re_path(r'^get_tables_postgresql/', views.tree_postgresql.get_tables, name='get_tables'),
    re_path(r'^get_schemas_postgresql/', views.tree_postgresql.get_schemas, name='get_schemas'),
    re_path(r'^get_columns_postgresql/', views.tree_postgresql.get_columns, name='get_columns'),
    re_path(r'^get_pk_postgresql/', views.tree_postgresql.get_pk, name='get_pk'),
    re_path(r'^get_pk_columns_postgresql/', views.tree_postgresql.get_pk_columns, name='get_pk_columns'),
    re_path(r'^get_fks_postgresql/', views.tree_postgresql.get_fks, name='get_fks'),
    re_path(r'^get_fks_columns_postgresql/', views.tree_postgresql.get_fks_columns, name='get_fks_columns'),
    re_path(r'^get_uniques_postgresql/', views.tree_postgresql.get_uniques, name='get_uniques'),
    re_path(r'^get_uniques_columns_postgresql/', views.tree_postgresql.get_uniques_columns, name='get_uniques_columns'),
    re_path(r'^get_indexes_postgresql/', views.tree_postgresql.get_indexes, name='get_indexes'),
    re_path(r'^get_indexes_columns_postgresql/', views.tree_postgresql.get_indexes_columns, name='get_indexes_columns'),
    re_path(r'^get_checks_postgresql/', views.tree_postgresql.get_checks, name='get_checks'),
    re_path(r'^get_excludes_postgresql/', views.tree_postgresql.get_excludes, name='get_excludes'),
    re_path(r'^get_rules_postgresql/', views.tree_postgresql.get_rules, name='get_rules'),
    re_path(r'^get_rule_definition_postgresql/', views.tree_postgresql.get_rule_definition, name='get_rule_definition'),
    re_path(r'^get_triggers_postgresql/', views.tree_postgresql.get_triggers, name='get_triggers'),
    re_path(r'^get_eventtriggers_postgresql/', views.tree_postgresql.get_eventtriggers, name='get_eventtriggers'),
    re_path(r'^get_inheriteds_postgresql/', views.tree_postgresql.get_inheriteds, name='get_inheriteds'),
    re_path(r'^get_inheriteds_parents_postgresql/', views.tree_postgresql.get_inheriteds_parents, name='get_inheriteds_parents'),
    re_path(r'^get_inheriteds_children_postgresql/', views.tree_postgresql.get_inheriteds_children, name='get_inheriteds_children'),
    re_path(r'^get_partitions_postgresql/', views.tree_postgresql.get_partitions, name='get_partitions'),
    re_path(r'^get_partitions_parents_postgresql/', views.tree_postgresql.get_partitions_parents, name='get_partitions_parents'),
    re_path(r'^get_partitions_children_postgresql/', views.tree_postgresql.get_partitions_children, name='get_partitions_children'),
    re_path(r'^get_statistics_postgresql/', views.tree_postgresql.get_statistics, name='get_statistics'),
    re_path(r'^get_statistics_columns_postgresql/', views.tree_postgresql.get_statistics_columns, name='get_statistics_columns'),
    re_path(r'^get_functions_postgresql/', views.tree_postgresql.get_functions, name='get_functions'),
    re_path(r'^get_function_fields_postgresql/', views.tree_postgresql.get_function_fields, name='get_function_fields'),
    re_path(r'^get_function_definition_postgresql/', views.tree_postgresql.get_function_definition, name='get_function_definition'),
    re_path(r'^get_function_debug_postgresql/', views.tree_postgresql.get_function_debug, name='get_function_debug'),
    re_path(r'^get_procedures_postgresql/', views.tree_postgresql.get_procedures, name='get_procedures'),
    re_path(r'^get_procedure_fields_postgresql/', views.tree_postgresql.get_procedure_fields, name='get_procedure_fields'),
    re_path(r'^get_procedure_definition_postgresql/', views.tree_postgresql.get_procedure_definition, name='get_procedure_definition'),
    re_path(r'^get_procedure_debug_postgresql/', views.tree_postgresql.get_procedure_debug, name='get_procedure_debug'),
    # new endpoint used by schema builder
    re_path(r'^get_table_definition_postgresql/', views.tree_postgresql.get_table_definition, name='get_table_definition'),
    re_path(r'^get_triggerfunctions_postgresql/', views.tree_postgresql.get_triggerfunctions, name='get_triggerfunctions'),
    re_path(r'^get_triggerfunction_definition_postgresql/', views.tree_postgresql.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    re_path(r'^get_eventtriggerfunctions_postgresql/', views.tree_postgresql.get_eventtriggerfunctions, name='get_eventtriggerfunctions'),
    re_path(r'^get_eventtriggerfunction_definition_postgresql/', views.tree_postgresql.get_eventtriggerfunction_definition, name='get_eventtriggerfunction_definition'),
    re_path(r'^get_aggregates_postgresql/', views.tree_postgresql.get_aggregates, name='get_aggregates'),
    re_path(r'^get_sequences_postgresql/', views.tree_postgresql.get_sequences, name='get_sequences'),
    re_path(r'^get_views_postgresql/', views.tree_postgresql.get_views, name='get_views'),
    re_path(r'^get_views_columns_postgresql/', views.tree_postgresql.get_views_columns, name='get_views_columns'),
    re_path(r'^get_view_definition_postgresql/', views.tree_postgresql.get_view_definition, name='get_view_definition'),
    re_path(r'^get_mviews_postgresql/', views.tree_postgresql.get_mviews, name='get_mviews'),
    re_path(r'^get_mviews_columns_postgresql/', views.tree_postgresql.get_mviews_columns, name='get_mviews_columns'),
    re_path(r'^get_mview_definition_postgresql/', views.tree_postgresql.get_mview_definition, name='get_mview_definition'),
    re_path(r'^get_databases_postgresql/', views.tree_postgresql.get_databases, name='get_databases'),
    re_path(r'^get_tablespaces_postgresql/', views.tree_postgresql.get_tablespaces, name='get_tablespaces'),
    re_path(r'^get_roles_postgresql/', views.tree_postgresql.get_roles, name='get_roles'),
    re_path(r'^get_extensions_postgresql/', views.tree_postgresql.get_extensions, name='get_extensions'),
    re_path(r'^get_extension_details/', views.tree_postgresql.get_extension_details, name='get_extension_details'),
    re_path(r'^save_postgresql_extension/', views.tree_postgresql.save_extension, name="save_postgresql_extension"),
    re_path(r'^get_available_extensions_postgresql/', views.tree_postgresql.get_available_extensions, name='get_available_extensions'),
    re_path(r'^get_physicalreplicationslots_postgresql/', views.tree_postgresql.get_physicalreplicationslots, name='get_physicalreplicationslots'),
    re_path(r'^get_logicalreplicationslots_postgresql/', views.tree_postgresql.get_logicalreplicationslots, name='get_logicalreplicationslots'),
    re_path(r'^get_publications_postgresql/', views.tree_postgresql.get_publications, name='get_publications'),
    re_path(r'^get_subscriptions_postgresql/', views.tree_postgresql.get_subscriptions, name='get_subscriptions'),
    re_path(r'^get_publication_tables_postgresql/', views.tree_postgresql.get_publication_tables, name='get_publication_tables'),
    re_path(r'^get_subscription_tables_postgresql/', views.tree_postgresql.get_subscription_tables, name='get_subscription_tables'),
    re_path(r'^get_foreign_data_wrappers_postgresql/', views.tree_postgresql.get_foreign_data_wrappers, name='get_foreign_data_wrappers'),
    re_path(r'^get_foreign_servers_postgresql/', views.tree_postgresql.get_foreign_servers, name='get_foreign_servers'),
    re_path(r'^get_user_mappings_postgresql/', views.tree_postgresql.get_user_mappings, name='get_user_mappings'),
    re_path(r'^get_foreign_tables_postgresql/', views.tree_postgresql.get_foreign_tables, name='get_foreign_tables'),
    re_path(r'^get_foreign_columns_postgresql/', views.tree_postgresql.get_foreign_columns, name='get_foreign_columns'),
    re_path(r'^get_types_postgresql/', views.tree_postgresql.get_types, name='get_types'),
    re_path(r'^get_domains_postgresql/', views.tree_postgresql.get_domains, name='get_domains'),
    re_path(r'^kill_backend_postgresql/', views.tree_postgresql.kill_backend, name='kill_backend'),
    re_path(r'^get_properties_postgresql/', views.tree_postgresql.get_properties, name='get_properties'),
    re_path(r'^get_database_objects_postgresql/', views.tree_postgresql.get_database_objects, name='get_database_objects'),
    re_path(r'^template_select_postgresql/', views.tree_postgresql.template_select, name='template_select'),
    re_path(r'^template_insert_postgresql/', views.tree_postgresql.template_insert, name='template_insert'),
    re_path(r'^template_update_postgresql/', views.tree_postgresql.template_update, name='template_update'),
    re_path(r'^template_select_function_postgresql/', views.tree_postgresql.template_select_function, name='template_select_function'),
    re_path(r'^template_call_procedure_postgresql/', views.tree_postgresql.template_call_procedure, name='template_call_procedure'),
    re_path(r'^change_active_database/', views.workspace.change_active_database, name='change_active_database'),
    re_path(r'^get_postgresql_version/', views.tree_postgresql.get_version, name='get_version'),
    re_path(r'^change_role_password_postgresql/', views.tree_postgresql.change_role_password, name='change_role_password'),
    re_path(r'^get_object_description_postgresql/', views.tree_postgresql.get_object_description, name='get_object_description'),\

    #PG_CRON
    re_path(r'^get_pgcron_jobs/', views.pgextras.get_pgcron_jobs, name='get_pgcron_jobs'),
    re_path(r'^get_pgcron_job_details/', views.pgextras.get_pgcron_job_details, name='get_pgcron_job_details'),
    re_path(r'^get_pgcron_job_logs/', views.pgextras.get_pgcron_job_logs, name='get_pgcron_job_logs'),
    re_path(r'^delete_pgcron_job_logs/', views.pgextras.delete_pgcron_job_logs, name='delete_pgcron_job_logs'),
    re_path(r'^save_pgcron_job/', views.pgextras.save_pgcron_job, name='save_pgcron_job'),
    re_path(r'^delete_pgcron_job/', views.pgextras.delete_pgcron_job, name='delete_pgcron_job'),

    #TREE_ORACLE
    re_path(r'^get_tree_info_oracle/', views.tree_oracle.get_tree_info, name='get_tree_info'),
    re_path(r'^get_tables_oracle/', views.tree_oracle.get_tables, name='get_tables'),
    re_path(r'^get_columns_oracle/', views.tree_oracle.get_columns, name='get_columns'),
    re_path(r'^get_pk_oracle/', views.tree_oracle.get_pk, name='get_pk'),
    re_path(r'^get_pk_columns_oracle/', views.tree_oracle.get_pk_columns, name='get_pk_columns'),
    re_path(r'^get_fks_oracle/', views.tree_oracle.get_fks, name='get_fks'),
    re_path(r'^get_fks_columns_oracle/', views.tree_oracle.get_fks_columns, name='get_fks_columns'),
    re_path(r'^get_uniques_oracle/', views.tree_oracle.get_uniques, name='get_uniques'),
    re_path(r'^get_uniques_columns_oracle/', views.tree_oracle.get_uniques_columns, name='get_uniques_columns'),
    re_path(r'^get_indexes_oracle/', views.tree_oracle.get_indexes, name='get_indexes'),
    re_path(r'^get_indexes_columns_oracle/', views.tree_oracle.get_indexes_columns, name='get_indexes_columns'),
    #re_path(r'^get_triggers_oracle/', views.tree_oracle.get_triggers, name='get_triggers'),
    #re_path(r'^get_partitions_oracle/', views.tree_oracle.get_partitions, name='get_partitions'),
    re_path(r'^get_functions_oracle/', views.tree_oracle.get_functions, name='get_functions'),
    re_path(r'^get_function_fields_oracle/', views.tree_oracle.get_function_fields, name='get_function_fields'),
    re_path(r'^get_function_definition_oracle/', views.tree_oracle.get_function_definition, name='get_function_definition'),
    re_path(r'^get_procedures_oracle/', views.tree_oracle.get_procedures, name='get_procedures'),
    re_path(r'^get_procedure_fields_oracle/', views.tree_oracle.get_procedure_fields, name='get_procedure_fields'),
    re_path(r'^get_procedure_definition_oracle/', views.tree_oracle.get_procedure_definition, name='get_procedure_definition'),
    #re_path(r'^get_function_debug_oracle/', views.tree_oracle.get_function_debug, name='get_function_debug'),
    #re_path(r'^get_triggerfunctions_oracle/', views.tree_oracle.get_triggerfunctions, name='get_triggerfunctions'),
    #re_path(r'^get_triggerfunction_definition_oracle/', views.tree_oracle.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    re_path(r'^get_sequences_oracle/', views.tree_oracle.get_sequences, name='get_sequences'),
    re_path(r'^get_views_oracle/', views.tree_oracle.get_views, name='get_views'),
    re_path(r'^get_views_columns_oracle/', views.tree_oracle.get_views_columns, name='get_views_columns'),
    re_path(r'^get_view_definition_oracle/', views.tree_oracle.get_view_definition, name='get_view_definition'),
    #re_path(r'^get_mviews_oracle/', views.tree_oracle.get_mviews, name='get_mviews'),
    #re_path(r'^get_mviews_columns_oracle/', views.tree_oracle.get_mviews_columns, name='get_mviews_columns'),
    #re_path(r'^get_mview_definition_oracle/', views.tree_oracle.get_mview_definition, name='get_mview_definition'),
    re_path(r'^get_tablespaces_oracle/', views.tree_oracle.get_tablespaces, name='get_tablespaces'),
    re_path(r'^get_roles_oracle/', views.tree_oracle.get_roles, name='get_roles'),
    re_path(r'^kill_backend_oracle/', views.tree_oracle.kill_backend, name='kill_backend'),
    re_path(r'^get_properties_oracle/', views.tree_oracle.get_properties, name='get_properties'),
    re_path(r'^template_select_oracle/', views.tree_oracle.template_select, name='template_select'),
    re_path(r'^template_insert_oracle/', views.tree_oracle.template_insert, name='template_insert'),
    re_path(r'^template_update_oracle/', views.tree_oracle.template_update, name='template_update'),

    #TREE_MYSQL
    re_path(r'^get_tree_info_mysql/', views.tree_mysql.get_tree_info, name='get_tree_info'),
    re_path(r'^get_tables_mysql/', views.tree_mysql.get_tables, name='get_tables'),
    re_path(r'^get_columns_mysql/', views.tree_mysql.get_columns, name='get_columns'),
    re_path(r'^get_pk_mysql/', views.tree_mysql.get_pk, name='get_pk'),
    re_path(r'^get_pk_columns_mysql/', views.tree_mysql.get_pk_columns, name='get_pk_columns'),
    re_path(r'^get_fks_mysql/', views.tree_mysql.get_fks, name='get_fks'),
    re_path(r'^get_fks_columns_mysql/', views.tree_mysql.get_fks_columns, name='get_fks_columns'),
    re_path(r'^get_uniques_mysql/', views.tree_mysql.get_uniques, name='get_uniques'),
    re_path(r'^get_uniques_columns_mysql/', views.tree_mysql.get_uniques_columns, name='get_uniques_columns'),
    re_path(r'^get_indexes_mysql/', views.tree_mysql.get_indexes, name='get_indexes'),
    re_path(r'^get_indexes_columns_mysql/', views.tree_mysql.get_indexes_columns, name='get_indexes_columns'),
    #re_path(r'^get_triggers_mysql/', views.tree_mysql.get_triggers, name='get_triggers'),
    #re_path(r'^get_partitions_mysql/', views.tree_mysql.get_partitions, name='get_partitions'),
    re_path(r'^get_functions_mysql/', views.tree_mysql.get_functions, name='get_functions'),
    re_path(r'^get_function_fields_mysql/', views.tree_mysql.get_function_fields, name='get_function_fields'),
    re_path(r'^get_function_definition_mysql/', views.tree_mysql.get_function_definition, name='get_function_definition'),
    re_path(r'^get_procedures_mysql/', views.tree_mysql.get_procedures, name='get_procedures'),
    re_path(r'^get_procedure_fields_mysql/', views.tree_mysql.get_procedure_fields, name='get_procedure_fields'),
    re_path(r'^get_procedure_definition_mysql/', views.tree_mysql.get_procedure_definition, name='get_procedure_definition'),
    #re_path(r'^get_function_debug_mysql/', views.tree_mysql.get_function_debug, name='get_function_debug'),
    #re_path(r'^get_triggerfunctions_mysql/', views.tree_mysql.get_triggerfunctions, name='get_triggerfunctions'),
    #re_path(r'^get_triggerfunction_definition_mysql/', views.tree_mysql.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    #re_path(r'^get_sequences_mysql/', views.tree_mysql.get_sequences, name='get_sequences'),
    re_path(r'^get_views_mysql/', views.tree_mysql.get_views, name='get_views'),
    re_path(r'^get_views_columns_mysql/', views.tree_mysql.get_views_columns, name='get_views_columns'),
    re_path(r'^get_view_definition_mysql/', views.tree_mysql.get_view_definition, name='get_view_definition'),
    re_path(r'^get_databases_mysql/', views.tree_mysql.get_databases, name='get_databases'),
    re_path(r'^get_roles_mysql/', views.tree_mysql.get_roles, name='get_roles'),
    re_path(r'^kill_backend_mysql/', views.tree_mysql.kill_backend, name='kill_backend'),
    re_path(r'^get_properties_mysql/', views.tree_mysql.get_properties, name='get_properties'),
    re_path(r'^template_select_mysql/', views.tree_mysql.template_select, name='template_select'),
    re_path(r'^template_insert_mysql/', views.tree_mysql.template_insert, name='template_insert'),
    re_path(r'^template_update_mysql/', views.tree_mysql.template_update, name='template_update'),

    #TREE_MARIADB
    re_path(r'^get_tree_info_mariadb/', views.tree_mariadb.get_tree_info, name='get_tree_info'),
    re_path(r'^get_tables_mariadb/', views.tree_mariadb.get_tables, name='get_tables'),
    re_path(r'^get_columns_mariadb/', views.tree_mariadb.get_columns, name='get_columns'),
    re_path(r'^get_pk_mariadb/', views.tree_mariadb.get_pk, name='get_pk'),
    re_path(r'^get_pk_columns_mariadb/', views.tree_mariadb.get_pk_columns, name='get_pk_columns'),
    re_path(r'^get_fks_mariadb/', views.tree_mariadb.get_fks, name='get_fks'),
    re_path(r'^get_fks_columns_mariadb/', views.tree_mariadb.get_fks_columns, name='get_fks_columns'),
    re_path(r'^get_uniques_mariadb/', views.tree_mariadb.get_uniques, name='get_uniques'),
    re_path(r'^get_uniques_columns_mariadb/', views.tree_mariadb.get_uniques_columns, name='get_uniques_columns'),
    re_path(r'^get_indexes_mariadb/', views.tree_mariadb.get_indexes, name='get_indexes'),
    re_path(r'^get_indexes_columns_mariadb/', views.tree_mariadb.get_indexes_columns, name='get_indexes_columns'),
    #re_path(r'^get_triggers_mariadb/', views.tree_mariadb.get_triggers, name='get_triggers'),
    #re_path(r'^get_partitions_mariadb/', views.tree_mariadb.get_partitions, name='get_partitions'),
    re_path(r'^get_functions_mariadb/', views.tree_mariadb.get_functions, name='get_functions'),
    re_path(r'^get_function_fields_mariadb/', views.tree_mariadb.get_function_fields, name='get_function_fields'),
    re_path(r'^get_function_definition_mariadb/', views.tree_mariadb.get_function_definition, name='get_function_definition'),
    re_path(r'^get_procedures_mariadb/', views.tree_mariadb.get_procedures, name='get_procedures'),
    re_path(r'^get_procedure_fields_mariadb/', views.tree_mariadb.get_procedure_fields, name='get_procedure_fields'),
    re_path(r'^get_procedure_definition_mariadb/', views.tree_mariadb.get_procedure_definition, name='get_procedure_definition'),
    #re_path(r'^get_function_debug_mariadb/', views.tree_mariadb.get_function_debug, name='get_function_debug'),
    #re_path(r'^get_triggerfunctions_mariadb/', views.tree_mariadb.get_triggerfunctions, name='get_triggerfunctions'),
    #re_path(r'^get_triggerfunction_definition_mariadb/', views.tree_mariadb.get_triggerfunction_definition, name='get_triggerfunction_definition'),
    re_path(r'^get_sequences_mariadb/', views.tree_mariadb.get_sequences, name='get_sequences'),
    re_path(r'^get_views_mariadb/', views.tree_mariadb.get_views, name='get_views'),
    re_path(r'^get_views_columns_mariadb/', views.tree_mariadb.get_views_columns, name='get_views_columns'),
    re_path(r'^get_view_definition_mariadb/', views.tree_mariadb.get_view_definition, name='get_view_definition'),
    re_path(r'^get_databases_mariadb/', views.tree_mariadb.get_databases, name='get_databases'),
    re_path(r'^get_roles_mariadb/', views.tree_mariadb.get_roles, name='get_roles'),
    re_path(r'^kill_backend_mariadb/', views.tree_mariadb.kill_backend, name='kill_backend'),
    re_path(r'^get_properties_mariadb/', views.tree_mariadb.get_properties, name='get_properties'),
    re_path(r'^template_select_mariadb/', views.tree_mariadb.template_select, name='template_select'),
    re_path(r'^template_insert_mariadb/', views.tree_mariadb.template_insert, name='template_insert'),
    re_path(r'^template_update_mariadb/', views.tree_mariadb.template_update, name='template_update'),

    #TREE_SQLITE
    re_path(r'^get_tree_info_sqlite/', views.tree_sqlite.get_tree_info, name='get_tree_info'),
    re_path(r'^get_tables_sqlite/', views.tree_sqlite.get_tables, name='get_tables'),
    re_path(r'^get_columns_sqlite/', views.tree_sqlite.get_columns, name='get_columns'),
    re_path(r'^get_pk_sqlite/', views.tree_sqlite.get_pk, name='get_pk'),
    re_path(r'^get_pk_columns_sqlite/', views.tree_sqlite.get_pk_columns, name='get_pk_columns'),
    re_path(r'^get_fks_sqlite/', views.tree_sqlite.get_fks, name='get_fks'),
    re_path(r'^get_fks_columns_sqlite/', views.tree_sqlite.get_fks_columns, name='get_fks_columns'),
    re_path(r'^get_uniques_sqlite/', views.tree_sqlite.get_uniques, name='get_uniques'),
    re_path(r'^get_uniques_columns_sqlite/', views.tree_sqlite.get_uniques_columns, name='get_uniques_columns'),
    re_path(r'^get_indexes_sqlite/', views.tree_sqlite.get_indexes, name='get_indexes'),
    re_path(r'^get_indexes_columns_sqlite/', views.tree_sqlite.get_indexes_columns, name='get_indexes_columns'),
    re_path(r'^get_triggers_sqlite/', views.tree_sqlite.get_triggers, name='get_triggers'),
    re_path(r'^get_views_sqlite/', views.tree_sqlite.get_views, name='get_views'),
    re_path(r'^get_views_columns_sqlite/', views.tree_sqlite.get_views_columns, name='get_views_columns'),
    re_path(r'^get_properties_sqlite/', views.tree_sqlite.get_properties, name='get_properties'),
    re_path(r'^template_select_sqlite/', views.tree_sqlite.template_select, name='template_select'),
    re_path(r'^template_insert_sqlite/', views.tree_sqlite.template_insert, name='template_insert'),
    re_path(r'^template_update_sqlite/', views.tree_sqlite.template_update, name='template_update'),

    #MONITORING SYSTEM
    re_path(r'^test_monitor_script/', views.monitor_dashboard.test_monitor_script, name='test_monitor_script'),
    re_path(r'^get_monitor_unit_list/', views.monitor_dashboard.get_monitor_unit_list, name='get_monitor_unit_list'),
    re_path(r'^get_monitor_unit_details/', views.monitor_dashboard.get_monitor_unit_details, name='get_monitor_unit_details'),
    re_path(r'^get_monitor_units/', views.monitor_dashboard.get_monitor_units, name='get_monitor_units'),
    re_path(r'^refresh_monitor_units/', views.monitor_dashboard.refresh_monitor_units, name='refresh_monitor_units'),
    re_path(r'^get_monitor_unit_template/', views.monitor_dashboard.get_monitor_unit_template, name='get_monitor_unit_template'),
    re_path(r'^save_monitor_unit/', views.monitor_dashboard.save_monitor_unit, name='save_monitor_unit'),
    re_path(r'^delete_monitor_unit/', views.monitor_dashboard.delete_monitor_unit, name='delete_monitor_unit'),
    re_path(r'^remove_saved_monitor_unit/', views.monitor_dashboard.remove_saved_monitor_unit, name='remove_saved_monitor_unit'),
    re_path(r'^update_saved_monitor_unit_interval/', views.monitor_dashboard.update_saved_monitor_unit_interval, name='update_saved_monitor_unit_interval'),

    # Configuration
    path('configuration/<int:config_id>/', views.configuration.delete_config, name="delete_configuration"),
    re_path(r'^configuration/$', views.configuration.get_configuration, name='get_configuration'),
    re_path(r'^configuration/categories/', views.configuration.get_configuration_categories, name='get_configuration_categories'),
    re_path(r'^save_configuration/', views.configuration.save_configuration, name='save_configuration'),
    re_path(r'^get_configuration_history/', views.configuration.get_configuration_history, name='get_configuration_history'),
    re_path(r'^configuration/status/', views.configuration.get_status, name="settings_status"),

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

    path('validate_binary_path/', views.workspace.validate_binary_path, name='validate_binary_path')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.PATH == '':
    v_url = ''
else:
    v_url = settings.PATH[1:] + '/'

urlpatterns = [# if you wish to maintain the un-prefixed URL's too
    re_path(v_url, include(base_urlpatterns)),
    #re_path(r'^subfolder/', include(base_urlpatterns))
]
