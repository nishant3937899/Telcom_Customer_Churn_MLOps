from MLOps_project import logger
import pandas as pd


class DataValidation:
    def __init__(self,config,schema):
        self.config=config
        self.schema=schema

    def data_validation(self):
        config=self.config
        schema=self.schema
        try:
            data = pd.read_csv(config.unzip_data_dir)
            all_col=list(data.columns)  

            all_schema_col=schema.column.keys()
            
            validation_status=True
            for col in all_col:
                if col not in all_schema_col:
                    validation_status=False
                    logger.error(f"Column {col} not found in schema!")
                    break
            for col in all_schema_col:
                if col not in all_col:
                    validation_status=False
                    logger.error(f'Column {col} is missing')

            with open(config.status_file,'w') as f:
                f.write(f'The validation status is : {validation_status}')
                
            if validation_status == True:
                logger.info('Validation was a success')
            else:
                logger.info('Validation was unsccessfull')
            return validation_status
        except Exception as e:
            raise e
