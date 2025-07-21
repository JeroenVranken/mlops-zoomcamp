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