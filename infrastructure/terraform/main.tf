# Configure the Google Cloud provider
provider "google" {
  project = var.project_id
  region  = var.region
}

# Create a Firestore database
resource "google_firestore_database" "firestore_database" {
  name     = var.firestore_database_name
  project  = var.project_id
  location = var.region
  type     = "FIRESTORE_NATIVE"

  # Ensure the Firestore API is enabled
  depends_on = [google_project_service.firestore]
}

# Create a Pub/Sub topic
resource "google_pubsub_topic" "pubsub_topic" {
  name    = var.pubsub_topic_name
  project = var.project_id

  # Ensure the Pub/Sub API is enabled
  depends_on = [google_project_service.pubsub]
}

# Create a Cloud Storage bucket
resource "google_storage_bucket" "storage_bucket" {
  name     = var.storage_bucket_name
  project  = var.project_id
  location = var.region

  # Configure versioning
  versioning {
    enabled = true
  }

  # Configure lifecycle rules (optional)
  lifecycle_rule {
    condition {
      age = 30 # days
    }
    action {
      type = "Delete"
    }
  }

  # Ensure the Storage API is enabled
  depends_on = [google_project_service.storage]
}

# Enable required APIs
resource "google_project_service" "firestore" {
  project = var.project_id
  service = "firestore.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "pubsub" {
  project = var.project_id
  service = "pubsub.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "storage" {
  project = var.project_id
  service = "storage-api.googleapis.com"

  disable_on_destroy = false
}

# HUMAN ASSISTANCE NEEDED
# The following resources may require additional configuration based on specific project requirements:
# 1. IAM roles and permissions for accessing the created resources
# 2. Network configuration (VPC, subnets, firewall rules)
# 3. Additional service accounts if needed
# 4. Monitoring and logging settings
# Please review and add these configurations as needed for your specific use case.