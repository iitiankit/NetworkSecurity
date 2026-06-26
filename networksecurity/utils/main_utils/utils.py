import yaml
import os,sys
from networksecurity.exception import CustomException
from networksecurity.logger import logging
import pickle

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys)
    
def write_yaml_file(file_path: str, data: dict):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "w") as file:
            yaml.safe_dump(data, file)

    except Exception as e:
        raise CustomException(e, sys)