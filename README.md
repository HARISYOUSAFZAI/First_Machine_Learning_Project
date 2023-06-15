# Machine_Learning_Project
This is the first machine learning project on github


**To install all the lib using that command**
pip install -r requirements.txt

**GIT COMMANDS**
1) To add all files "git add ." 
2) To add selected files "git add 'file name'"
3) To check the status "git status"
4) To check the version of the git "git log"
5) to create a new version/commit all changes by git "git commit -m "MESSAGE" "
6) to send changes/version to github "git push origin main"
7) to check the remote url "get remote -v"

**HEROKU**
To setup CI/CD pipeline in heroku we need 3 information 

1. HEROKU_EMAIL =  
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = ml-regression

**DOCKER**
Build docker image

docker build -t <image_name>:<tagname> .
>Note: Image name for docker must be lowercase.


**Python Libraries**
Python libraries installation command

python setup.py install
or 
pip install requirement.txt

Note: -e . has been added in the requirement.txt because it will install the package which is housing (setup.py)

**Working on Different Packages**

1. Logger
2. Exception
3. Components (data_ingestion.py, data_validation.py,etc .. )
4. pipeline (pipline.py) (the blocks inside the components are called pipeline)
5. Entity (Table or any data or object generated during ML experiment because of pipline it is also called artefact)
6. Config (To perform or initiate some task we need some inputs it is called confiugration, it can be DataingestionConfig etc )

***Steps of the ML project***

1. **Data Ingestion:** Bring data into System and split dataset into two parts (train and test dataset)

2. **Data validation:** Data range imbalanced Dataset, Outliers, Duplicate data, 
                Schema Validation, Null check, Domain value, Anomalies (**Jupyter**)  

3. **Data Transformation:** Performing EDA to understanding data (**Jupyter**)
   (saving an object into a file is called serialization & loading object from file is called as deserialization)(Pickle Objecti of feature engineering )
4. **Model Training:** Model Selection (Model Evaluation)
                Hyperparameter tuning (Pickle Object of Model Training)
5. **Model Comparison:** Comparison with best model and minimum expectation 

6. **Models Evaluation:** Test dataset for model Evaluation 

Real World dataset >> Pickle object of feature engineering (transform function) >> Transfored dataset >> Pickle Object of Model Training>> Predict Function >> Prediction 

**MLOps >> DevOps**

**DEVOps:** (Code Versioning and DevOps is the combination of cultureal philosophies, practices, and tools that increases an organization's ability to deliver applications and services at high velcity  )
(CI:Continuous integration + CD: Continuous Deployment)

**MLOps:** DAta Versioning (CT:continuous training)


**Data Versioning:** based on timestamp and hash file.

