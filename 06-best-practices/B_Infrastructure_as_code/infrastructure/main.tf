terraform {
    required_version = ">= 1.0.0"
    backend "s3" {
        bucket  = "tf-state-mlops-zoomcamp-b"
        key     = "mlops-zoomcamp.tfstate"
        region  = "eu-west-3"
        encrypt = true
        
      
    }
}

provider "aws" {
    region = var.aws_region
}

data "aws_caller_identity" "current_identity" {}

locals {
    account_id = data.aws_caller_identity.current_identity.account_id
}


# ride_events
module "source_kinesis_stream" {
    source = "./modules/kinesis"
    retention_period = 24
    shard_count = 2
    stream_name = "${var.source_stream_name}_${var.project_id}"
    tags = var.project_id
}

# ride_predictions
module "output_kinesis_stream" {
    source = "./modules/kinesis"
    retention_period = 24
    shard_count = 2
    stream_name = "${var.output_stream_name}_${var.project_id}"
    tags = var.project_id
}

# Model bucket
module "s3_bucket" {
    source = "./modules/s3"
    bucket_name = "${var.model_bucket}-${var.project_id}"
}

# ECR repository
module "ecr_image" {
    source = "./modules/ecr"
    ecr_repo_name = "${var.ecr_repo_name}-${var.project_id}"
    account_id = local.account_id
    lambda_function_local_path = var.lambda_function_local_path
    docker_image_local_path = var.docker_image_local_path
    region = var.aws_region
    
}

module "lambda_function" {
    source = "./modules/lambda"
    image_uri = module.ecr_image.image_uri
    lambda_function_name = "${var.lambda_function_name}_${var.project_id}"
    model_bucket = module.s3_bucket.name
    output_stream_name = "${var.output_stream_name}_${var.project_id}" 
    output_stream_arn = module.output_kinesis_stream.stream_arn
    source_stream_name = "${var.source_stream_name}_${var.project_id}"
    source_stream_arn = module.source_kinesis_stream.stream_arn
}