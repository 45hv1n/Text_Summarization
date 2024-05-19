from Text_Summarization.entity import DataValidationConfig
from Text_Summarization.logging import logger
import os 
from pathlib import Path

class DataValidator:

    def __init__(self, config: DataValidationConfig):
        self.config_model = config

    def validate_data(self) -> bool:
        try :
            validaton_status = None
            all_file_path = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_file_path:
                logger.info(f"\n\n vaasadadadad: Validation Status: {validaton_status} \n\n")
                if file not in self.config_model.ALL_FILES_REQUIRED:
                    validaton_status = False
                    with open(self.config_model.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validaton_status}")
                else:
                    validaton_status = True
                    with open(self.config_model.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validaton_status}")
            #return validaton_status

        except Exception as e:
            raise e
            