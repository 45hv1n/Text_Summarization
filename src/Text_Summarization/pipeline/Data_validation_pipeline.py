from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.Data_Validation import DataValidator


class DataValidationPipeline:
    
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        dataValidation_model = config.get_data_validation_config()

        #logger.info(f"aaaaaaajfjfjfjfjfjfjfjfj {dataValidation_model}")


        data_validator = DataValidator(config= dataValidation_model)
        data_validator.validate_data()