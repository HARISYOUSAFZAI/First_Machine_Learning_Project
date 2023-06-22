
from housing.pipline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import sys,os
from housing.config.configuration import Configuration


def main():
    try:
        pipe = Pipeline()
        pipe.run_pipeline()
        data_validation_config = Configuration().get_data_validation_config()
        logging.info(f"{data_validation_config}")
        
    except Exception as e:
        logging.error(f"{e}")
        raise HousingException(e,sys) from e
        print(e)    

if __name__=="__main__":
    main()