
source_stream_name = "stg_ride_events"
output_stream_name = "stg_ride_predictions"
model_bucket = "stg-mlflow-models-jer"
lambda_function_local_path = "../code/lambda_function.py"
docker_image_local_path = "../code/Dockerfile"
pipfile_lock_local_path = "../code/Pipfile.lock"
ecr_repo_name = "stg_stream_model_duration"
lambda_function_name = "stg_ride_predictions_lambda"