import os
from src.logger import get_logger
from src.custom_exception import CustomException
import pandas as pd
import yaml

logger = get_logger(__name__)


def read_yaml(file_path):
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not found in the given path")
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the yaml file")
            return config
        
    except Exception as e:
        logger.error("Error occur while reading yaml file")
        raise CustomException("Fail to read yaml file", e)
    

def load_data(path):
    try:
        logger.info("Load the data")
        return pd.read_csv(path)
    except Exception as e:
        logger.info("Error occour while loading the data")
        raise CustomException("Failed to load data", e)
    

