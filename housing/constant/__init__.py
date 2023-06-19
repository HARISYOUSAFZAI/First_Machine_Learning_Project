import os
from datetime import datetime
ROOT_DIR = os.chdir('e:\\PyCharm\\First_Machine_Learning_Project\\')
ROOT_DIR = os.getcwd()  # to current working directory
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%m-%S')}"

# Training pipeline related  variable

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# Data Ingestion related variables

DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"


# Data validation related Variables

DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_FILE_PATH_KEY = "schema_file_path"

#Data transformation related Variables

DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORMATION_CONGIF_KEY = "data_transformation_config"
DATA_TRANSFORMATION_TRAIN_DIR_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY =  "transformed_dir"
DATA_TRANSFORMATION_TEST_DIR_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPORCESSED_DIR_KEY = "preprocessed_dir"
DATA_TRANSFORMATION_PREPORCESSED_OBJECT_PATH_KEY =  "preprocessed_object_file_path"
DATA_TRANSFORMATION_BEDROOM_PER_ROOM_KEY = "add_bedroom_per_room"

# Model trainer related variables"

MODEL_TRAINER_ARTIFACT_DIR = "model_training"
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_TRAINED_DIR_KEY = "trained_model_model_dir"
MODEL_TRAINER_BASE_ACCURACY_KEY = "base_accuracy"

# Model push related variables

MODEL_PUSH_ARTIFACT_DIR = "model_push"
MODEL_PUSH_CONFIG_KEY = "model_pusher_config"
MODEL_PUSH_EXPORT_DIR_KEY = "model_export_dir"


# Model evaluaation related variables

MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"


