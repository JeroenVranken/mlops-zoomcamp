variable "ecr_repo_name" {
  description = "The name of the ECR repository to create."
  type        = string
}



variable "ecr_image_tag" {
    type        = string
    description = "ECR repo name"
    default = "latest"
}

variable "lambda_function_local_path" {
    type        = string
    description = "Local path to lambda function / python file"
}

variable "docker_image_local_path" {
    type        = string
    description = "Local path to Dockerfile"
}

variable "region" {
    type        = string
    description = "region"
    default = "eu-west-3"
}

variable "account_id" {
}