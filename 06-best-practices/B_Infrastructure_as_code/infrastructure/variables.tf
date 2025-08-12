variable "aws_region" {
    description = "AWS region"
    default = "eu-west-3"
}

variable "project_id" {
    description = "Project ID"
    default = "mlops-zoomcamp"
}

variable "source_stream_name" {
    description = "Source Kinesis stream name"
}

variable "output_stream_name" {
    description = "Output Kinesis stream name"
}


variable "model_bucket" {
    description = "Name of the S3 bucket"
}

variable "lambda_function_local_path" {
  description = ""
}

variable "docker_image_local_path" {
  description = ""
}

variable "ecr_repo_name" {
  description = ""
}

variable "lambda_function_name" {
  description = ""
}