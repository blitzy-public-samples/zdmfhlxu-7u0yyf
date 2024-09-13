output "firestore_database_url" {
  value       = google_firestore_database.firestore_database.self_link
  description = "The URL of the Firestore database"
}

output "pubsub_topic_id" {
  value       = google_pubsub_topic.pubsub_topic.id
  description = "The ID of the Pub/Sub topic"
}

output "storage_bucket_url" {
  value       = google_storage_bucket.storage_bucket.url
  description = "The URL of the Cloud Storage bucket"
}