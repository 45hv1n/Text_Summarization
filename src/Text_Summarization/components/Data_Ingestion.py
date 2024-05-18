import os
from urllib import request
import zipfile
from Text_Summarization.logging import logging
from Text_Summarization.utils.common import get_size
from Text_Summarization.entity import DataIngestionConfig

class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    
    def download_files(self):

        if not os.path.exists(self.data_ingestion_config.local_dir_file):
            filename, headers = request.urlretrieve(
                url = self.data_ingestion_config.source_url,
                filename = self.data_ingestion_config.local_dir_file
            )
            logging.info(f"{filename} download with following info \n{headers}")
        else:
            logging.info("File already exist")

    def extract_zip_file(self):

        unzip_path = self.data_ingestion_config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.data_ingestion_config.local_dir_file, 'r') as zipref:
            zipref.extractall(unzip_path)