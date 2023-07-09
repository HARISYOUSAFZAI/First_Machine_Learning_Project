from housing.entity.config_entity import *
from housing.entity.artifact_entity import *
from housing.exception import HousingException
import sys,os
from housing.logger import logging
import shutil

class ModelPusher:


    def __init__(self,
                  model_pusher_config: ModelPusherConfig,
                  model_evaluation_artifact: ModelEvaluationArtifact 
                  ):
        try:
            logging.info(f"{'>>' * 30} Model Pusher log started. {'<<' * 30}")
            self.model_pusher_config = model_pusher_config
            self.model_evaluation_artifact = model_evaluation_artifact

        except Exception as e:
            raise HousingException(e,sys) from e
    def export_model(self) -> ModelPusherArtifact:
        try:
            evaluated_model_file_path = self.model_evaluation_artifact.evaluated_model_path
            export_dir = self.model_pusher_config.export_dir_path
            model_file_name = os.path.basename(evaluated_model_file_path)
            export_model_file_path = os.path.join(export_dir, model_file_name)
            logging.info(f"Exporting model file: [{export_model_file_path}]")
            os.makedirs(export_dir,exist_ok= True)

            # we can call a function to save a model to Azure blob storage or google cloud/ Amazon s3 bucket
            #instead of shutil.copy we can save in cloud

            # ===========create a function ==========
            # to save a model in cloud
            #========================================

            shutil.copy(src = evaluated_model_file_path,dst= export_model_file_path)

            logging.info(f"Train model: {evaluated_model_file_path} is copied in export dir: [{export_model_file_path}]")

            model_pusher_artifact = ModelPusherArtifact(is_moder_pusher= True,
                                                        export_model_file_path=export_model_file_path
                                                        )
            logging.info(f"Model pusher artifact: [{model_pusher_artifact}]")
            return model_pusher_artifact
        
        except Exception as e:
            raise HousingException(e,sys) from e
    def inititate_model_pusher(self) -> ModelPusherArtifact:
        try:
            return self.export_model()
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def __del__(self):
        logging.info(f"{'>>' * 20}Model Pusher log is completed.{'<<' * 20}")

        
