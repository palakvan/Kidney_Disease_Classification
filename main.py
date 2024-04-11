from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/palakvan/Kidney_Disease_Classification.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="palakvan"
os.environ["MLFLOW_TRACKING_PASSWORD"]="038196cf537e025d3694b350d62495e26ff48315"



# STAGE_NAME = "Data Ingestion stage"
# try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#         data_ingestion = DataIngestionTrainingPipeline()
#         data_ingestion.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e
    
# STAGE_NAME = "Prepare Base Model"
# try: 
#         logger.info(f"*******************")
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = PrepareBaseModelTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e

STAGE_NAME = "Training"
try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e