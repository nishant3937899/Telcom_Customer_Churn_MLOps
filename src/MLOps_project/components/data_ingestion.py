import os
import zipfile
import urllib.request as request
from MLOps_project import logger



class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.zip_downl_loc):
            filename, header = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.zip_downl_loc
            )
            logger.info(f"Downloaded {filename}")
        else:
            logger.info("File already exists")

    def unzip_data(self):
        os.makedirs(self.config.unzip_dir_loc, exist_ok=True)
        with zipfile.ZipFile(self.config.zip_downl_loc, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir_loc)

        logger.info("Data extracted")