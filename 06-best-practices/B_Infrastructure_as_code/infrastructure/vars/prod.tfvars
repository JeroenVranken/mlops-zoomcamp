
source_stream_name = "prod_ride_events"
output_stream_name = "prod_ride_predictions"
model_bucket = "prod-mlflow-models-jer"
lambda_function_local_path = "../code/lambda_function.py"
docker_image_local_path = "../code/Dockerfile"
pipfile_lock_local_path = "../code/Pipfile.lock"
ecr_repo_name = "prod_stream_model_duration"
lambda_function_name = "prod_ride_predictions_lambda"