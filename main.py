from Text_Summarization.pipeline.Data_ingestion_pipeline import DataIngestionPipeline
from Text_Summarization.logging import logger

STAGE_NAME = "DATA INGESTION STAGE."

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e