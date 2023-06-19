
from housing.pipline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import sys,os


def main():
    try:
        pipe = Pipeline()
        pipe.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        raise HousingException(e,sys) from e
        print(e)    

if __name__=="__main__":
    main()