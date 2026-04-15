from MLOps_project.components.data_validation import DataValidation
from MLOps_project.config.configuration import config_mgr_val
from MLOps_project import logger

def run_data_validation():
    try:
        data_val=config_mgr_val()
        config,schema=data_val.create_validation_dir()
        validation=DataValidation(config,schema)
        validation.data_validation()

    except Exception as e:
        raise e
    

if __name__ == '__main__':
    stage_name= 'DATA VALIDATION'
    try:
        logger.info(f'stage : {stage_name} has successfully started')
        run_data_validation()
        logger.info(f'stage : {stage_name} has successfully completed')
    except Exception as e:
        raise e