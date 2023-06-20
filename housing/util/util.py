import yaml
from housing.exception import HousingException
import sys, os



def read_yaml_file(file_path: str) -> dict:
    """
    Read a  YAML file and return the contents as a dictionary
    :param file_path: str
    :return: dict
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e
