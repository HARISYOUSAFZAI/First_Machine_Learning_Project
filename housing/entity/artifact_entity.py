from collections import namedtuple


DataIngestionArtifact = namedtuple ("DataIngestionArtifact", 
                                    ["train_file_path",
                                     "test_file_path",
                                     "is_ingested",
                                     "message"]
                                     )

DataValidationArtifact = namedtuple("DataValidationArtifact",
                                    ["schema_file_path",
                                     "report_file_path",
                                     "report_page_file_path",
                                     "is_validated","message"]
                                     )

DataTransformationArtifact = namedtuple("DataTransfromationArtifact",
                                       ["transformed_train_file_path",
                                        "transformed_test_file_path",
                                       "is_transformed".
                                       "messsage",
                                       "preprocessed_object_file_path"]
                                       )

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",
                                   ["is_trained", 
                                    "trained_model_file_path",
                                    "train_rmsc",
                                    "train_accuracy",
                                    "test_accuracy",
                                    "model_accuracy"]
                                    )

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact",
                                      ["evaluated_model_path",
                                      "is_model_accepted"]
                                      )

ModelPusherArtifact = namedtuple ("ModelPusherArtifact",
                                  ["is_moder_pusher",
                                   "export_model_file_path"]
                                   )

