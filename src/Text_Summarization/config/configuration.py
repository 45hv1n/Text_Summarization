from Text_Summarization.constants import *
from Text_Summarization.utils.common import read_yaml, create_directories
from pathlib import Path
from Text_Summarization.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH
        ):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config_model = self.config.data_ingestion

        create_directories([config_model.root_dir])

        data_ingestion_model = DataIngestionConfig(
            root_dir= config_model.root_dir,
            source_url= config_model.source_url,
            local_dir_file= config_model.local_data_file,
            unzip_dir= config_model.unzip_dir
        )

        return data_ingestion_model
        