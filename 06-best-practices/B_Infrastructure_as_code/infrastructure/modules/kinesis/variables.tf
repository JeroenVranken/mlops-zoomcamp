variable "stream_name" {
    type = string
    description =  "Kinesis stream name"
}

variable "shard_count" {
    type = number
    description =  "Kinesis stream number of shards"
}

variable "retention_period" {
    type = number
    description =  "Kinesis stream retention period"
}

variable "shard_level_metrics" {
    type = list(string)
    description =  "Kinesis stream shard level metrics"
    default =  [
        "IncomingBytes",
        "IncomingRecords",
        "OutgoingBytes",
        "OutgoingRecords",
        "WriteProvisionedThroughputExceeded",
        "ReadProvisionedThroughputExceeded",
        "IteratorAgeMilliseconds",
    ]
}

variable "tags" {
    description = "Tags for Kinesis stream"
    default = "mlops-zoomcamp"
}