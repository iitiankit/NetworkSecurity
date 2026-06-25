import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.logger import logging
from networksecurity.exception import CustomException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def csv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            logging.info("File readed from csv")
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data(self,database,collection,records):
        try:
            self.database = database
            self.collections = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info("Connection Succesful")
            self.database = self.mongo_client[self.database]

            self.collections = self.database[self.collections]
            self.collections.insert_many(records)
            logging.info("Records Pushed")

            return len(self.records)
        
        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    try:
        FILE_PATH="Network_Data\phisingData.csv"
        DATABASE="ANKITDB"
        Collection="NetworkData"
        obj = NetworkDataExtract()
        records = obj.csv_to_json(file_path=FILE_PATH)
        len = obj.insert_data(DATABASE,Collection,records)

        print(len)

    except Exception as e:
        raise CustomException(e,sys)
    

        