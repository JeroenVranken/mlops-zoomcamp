
variable output_stream_arn {
  description = "The ARN of the output stream for the Lambda function."
  type        = string
}

variable model_bucket {
  description = "The name of the S3 bucket where the model is stored."
  type        = string
}

variable "output_stream_name" {
  description = "Name of output stream where all the events will be passed"
}

variable "lambda_function_name" {
  description = "Name of the lambda function"
}

variable "image_uri" {
  description = "ECR image uri"
}

variable "source_stream_name" {
  description = "Name of the source stream for the Lambda function."
  type        = string
}

variable "source_stream_arn" {
  description = "The ARN of the source stream for the Lambda function."
  type        = string
}