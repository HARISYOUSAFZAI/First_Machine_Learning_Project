from setuptools import setup
from typing import List


def get_requirements_list() -> List[str]:
    """
        Description: this function is going to return list of requirement
        mention is requirement.txt file
        
        return: This function is going to return a list which contain name 
        of libraries mentioned is requirement.txt
    """
    with open("requirement.txt") as requirement_file:
        return requirement_file.readlines()


setup(
    name="housing-predictor",
    version="0.0.1",
    author="hy",
    description="This is the first End to End pipline ML project",
    packages=["housing"],
    install_requires=get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())
