from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from src.components.data_transformation import DataTransformer

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data ingestion initiated')
        try:
            df = pd.read_csv('notebooks/data/stud.csv')
            logging.info('Read csv data')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            logging.info('Saved raw data to artifact')

            train_set, test_set = train_test_split(df,test_size=0.2, random_state=42)
            logging.info('Train test split initiated')

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Saved Train / test data to artifact')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()
    transform = DataTransformer()
    transform.initiate_data_transformation(train_path=train_path, test_path=test_path)