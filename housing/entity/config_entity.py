from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["dataset_download_url", "tgz_download_dir", "raw_data_dir",
                                  "ingested_train_dir", "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",
                                  ["schema_file_path",
                                   "report_file_path",
                                   "report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",
                                      ["add_bedroom_per_room", "transformed_train_dir", "transformed_test_dir",
                                       "preprocessed_object_file_path"])

# add_bedroom_per_room (Boolean),
# transform_train_dir (applying feature engineering on ingested train data and save it here),
# "transformed_test_dir" (applying feature engineering on ingested test data and save it here),
# "preprocessed_object_file_path (save all the steps of feature engineering in the form of pickle object)

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path", "base_accuracy","model_config_file_path"])

# trained_model_file_path (save the trained model which has high accuracy in the form of pickle)
# base_accuracy (the base accuracy matrix will save here)

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path", 'time_stamp'])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])