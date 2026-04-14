from pathlib import Path
from MLOps_project.utils.common import read_yaml,createDIr
from MLOps_project import logger
class ConfigManager:
    def __init__(self):
        self.config = read_yaml(Path("config/config.yaml"))
        self.params = read_yaml(Path("params.yaml"))
        self.schema = read_yaml(Path("schema.yaml"))

    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        createDIr([config.rootdir_zip_down])
        logger.info(f'{config.rootdir_zip_down} has successfully created')

        return config