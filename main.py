from MLOps_project import logger
from MLOps_project.pipeline.stage_01_data_ingestion import run_data_ingestion

stage_name='DATA INGESTION'
try:
    logger.info(f'stage : {stage_name} has successfully started')
    run_data_ingestion()
    logger.info(f'stage : {stage_name} has successfully completed')
except Exception as e:
    raise e
