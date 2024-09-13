#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Load environment variables
source .env

# Build Docker images
echo "Building Docker images..."
docker build -t gcr.io/${PROJECT_ID}/backend:latest -f infrastructure/docker/Dockerfile.backend .
docker build -t gcr.io/${PROJECT_ID}/frontend:latest -f infrastructure/docker/Dockerfile.frontend .

# Push Docker images to Google Container Registry
echo "Pushing Docker images to Google Container Registry..."
docker push gcr.io/${PROJECT_ID}/backend:latest
docker push gcr.io/${PROJECT_ID}/frontend:latest

# Apply Terraform configurations
echo "Applying Terraform configurations..."
cd infrastructure/terraform
terraform init
terraform apply -auto-approve

# Deploy services to Google Cloud Run
echo "Deploying services to Google Cloud Run..."
gcloud run deploy backend \
    --image gcr.io/${PROJECT_ID}/backend:latest \
    --platform managed \
    --region ${REGION} \
    --allow-unauthenticated

gcloud run deploy frontend \
    --image gcr.io/${PROJECT_ID}/frontend:latest \
    --platform managed \
    --region ${REGION} \
    --allow-unauthenticated

echo "Deployment completed successfully!"

# HUMAN ASSISTANCE NEEDED
# The following steps may require additional configuration or manual intervention:
# 1. Ensure that the necessary environment variables are set in the .env file
# 2. Make sure the user has the required permissions to push to GCR and deploy to Cloud Run
# 3. Verify that the Terraform configurations are up-to-date and match the desired infrastructure
# 4. Consider adding additional error handling and logging for production use