from resource_management.core.resources.system import Directory, File
from resource_management.libraries.functions.format import format
from resource_management.core.source import Template


def setup_solr():
    import params

    Directory([params.solr_config_dir, params.solr_config_log_dir, params.solr_config_service_log_dir,
               params.solr_config_pid_dir, params.solr_config_conf_dir],
              mode=0755,
              cd_access='a',
              owner=params.solr_config_user,
              group=params.solr_config_group,
              create_parents=True
              )

    File(format("{solr_config_bin_dir}/solr.in.sh"),
         content=Template("solr.in.sh.j2"),
         owner=params.solr_config_user
         )

    File(format("{solr_config_conf_dir}/log4j.properties"),
         content=Template("log4j.properties.j2"),
         owner=params.solr_config_user
         )