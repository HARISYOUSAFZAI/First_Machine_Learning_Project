# first step is to check the data is available in test and train directory

from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from housing.constant import *
import os,sys
import pandas as pd
import numpy as np
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json


class DataValidation:

    def __init__(self, data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact ) ->None:
        try:
            
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise  HousingException(e,sys) from e

    def is_train_test_file_exsits(self) -> bool:
        try:
            logging.info("Checking the test and train file existance")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_test_file_exist and is_train_file_exist

            logging.info(f"the test and train file exist?  '{is_available}'")

            if not is_available:
                train_file = self.data_ingestion_artifact.train_file_path
                test_file = self.data_ingestion_artifact.test_file_path
                message = f"Training {train_file} or Testing {test_file}" \
                      "file is not present in the following locations" 
                logging.info(message)
                raise Exception(message)

            return is_available


        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df,test_df
        except Exception as e :
            raise HousingException(e,sys) from e

    def validate_dataset_schema(self) -> bool:
        try:
            validation_status = False

            # if self.is_train_test_file_exsits():
            #     train_dir = self.data_ingestion_artifact.train_file_path
            #     test_dir = self.data_ingestion_artifact.test_file_path

            #     train_dataset_path = os.path.join(train_dir,TRAIN_DATASET)
            #     test_dataset_path = os.path.join(test_dir,TEST_DATASET)

            #     train_df = pd.read_csv(train_dataset_path)
            #     test_df = pd.read_csv(test_dataset_path)

            #     validation_schema_path = os.path.join(ROOT_DIR)
                #validation_schema = 
                # 1.Number of column
                # 2.check the value of ocean proximity
                #         * acceptable values(category)
                # 3.check column names


            validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def is_data_drift_found(self):
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def detect_outliers_from_train_data(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
        
    def get_and_save_data_drift_report(self):
        try:
            profile = Profile (sections = [DataDriftProfileSection()])

            train_df,test_df = self.get_train_and_test_df()
            
            profile.calculate(train_df,test_df)

            profile.json()

            report = json.loads(profile.json())

            #os.makedirs(self.data_validation_artifact.report_file_path,exist_ok=True)
            report_file_path = self.data_validation_config.report_file_path

            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path, "w") as report_file:
                json.dump(report, report_file , indent = 6)
            return report
            
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def save_data_drift_report_page(self):
        try:

            train_df,test_df = self.get_train_and_test_df()

            dashboard = Dashboard(tabs=[DataDriftTab()])
            dashboard.calculate(train_df,test_df)
            
            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)

        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exsits()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated= True,
                message="Data Validation performed successfully"
            )
            logging.info (f"Data_validation_artifact {data_validation_artifact}")
            
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        

    def __del__(self):
        logging.info(f"{'='*20} Data validation log completed {'='*20}")