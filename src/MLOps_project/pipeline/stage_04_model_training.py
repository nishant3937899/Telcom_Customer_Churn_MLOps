
from MLOps_project.config.configuration import  config_trainer
from MLOps_project.components.model_trainer import model_trainer,model_training
from MLOps_project import logger



def model_train():
    try:
        dir_create=config_trainer()
        config= dir_create.create_trainer_dir()
        model_train=model_training(config)
        train=model_train.model_train_start()
    except Exception as e:
        raise e





if __name__ == '__main__':
    stage_name= 'MODEL TRAINING'
    try:
        logger.info(f'stage : {stage_name} has successfully started')
        model_train()
        logger.info(f'stage : {stage_name} has successfully completed')
    except Exception as e:
        raise e