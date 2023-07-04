
from housing.pipline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import sys,os
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        pipe = Pipeline()
        pipe.run_pipeline()
        # data_transformation_config = Configuration().get_data_transformation_config()
        # logging.info(f"{data_transformation_config}")
        # schema_file_path = r"E:\PyCharm\First_Machine_Learning_Project\Config\schema.yaml"
        # file_path = r"E:\PyCharm\First_Machine_Learning_Project\housing\artifact\data_ingestion\2023-06-21_19-06-43\ingested_data\train\housing.csv"

        # df =DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        raise HousingException(e,sys) from e
        print(e)    

if __name__=="__main__":
    main()