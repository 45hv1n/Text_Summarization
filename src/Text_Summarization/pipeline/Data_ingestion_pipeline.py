from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.entity import DataIngestionConfig
from Text_Summarization.components.Data_Ingestion import DataIngestion
from Text_Summarization.logging import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config_model = config_manager.get_data_ingestion_config()
        
        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config_model)
        data_ingestion.download_files()
        data_ingestion.extract_zip_file()
