variable "project_id" {
  type        = string
  description = "The ID of the Google Cloud project."
}

variable "region" {
  type        = string
  description = "The region where resources will be deployed."
}

variable "firestore_database_name" {
  type        = string
  description = "The name of the Firestore database."
}

variable "pubsub_topic_name" {
  type        = string
  description = "The name of the Pub/Sub topic."
}

variable "storage_bucket_name" {
  type        = string
  description = "The name of the Cloud Storage bucket."
}