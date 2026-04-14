from MLOps_project.components.data_ingestion import DataIngestion
from MLOps_project.config.configuration import ConfigManager
from MLOps_project import logger


stage_name="Data Ingestion"
def run_data_ingestion():
    try:
        dataingestion_config=ConfigManager()
        DataIngestion_mgr=dataingestion_config.get_data_ingestion_config()

        data_ingestion=DataIngestion(DataIngestion_mgr)
        final_data=data_ingestion.download_file()
        final_data=data_ingestion.unzip_data()
        logger.info(f'data has successfully ingested')

    except Exception as e:
        raise e
    
if __name__ == '__main__':
    try:
        logger.info(f'stage : {stage_name} has successfully started')
        run_data_ingestion()
        logger.info(f'stage : {stage_name} has successfully completed')
    except Exception as e:
        raise e