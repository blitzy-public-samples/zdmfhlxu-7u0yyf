#!/bin/bash

# Setup script for GitHub Repository Scanner

# Exit immediately if a command exits with a non-zero status
set -e

# Function to print messages
print_message() {
    echo "===> $1"
}

# Install backend dependencies
print_message "Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

# Install frontend dependencies
print_message "Installing frontend dependencies..."
cd frontend
npm install
cd ..

# Set up environment variables
print_message "Setting up environment variables..."
cat << EOF > .env
# Backend environment variables
GITHUB_API_KEY=your_github_api_key_here
FIRESTORE_PROJECT_ID=your_firestore_project_id_here
EMAIL_SENDER=your_email_sender_here
EMAIL_RECIPIENT=your_email_recipient_here

# Frontend environment variables
REACT_APP_API_URL=http://localhost:8000
EOF

print_message "Environment variables have been set up. Please update the values in the .env file."

# Initialize local services for testing
print_message "Initializing local services for testing..."

# Check if Google Cloud SDK is installed
if ! command -v gcloud &> /dev/null
then
    print_message "Google Cloud SDK is not installed. Please install it to use local emulators."
    print_message "Visit https://cloud.google.com/sdk/docs/install for installation instructions."
else
    # Start Firestore emulator
    print_message "Starting Firestore emulator..."
    gcloud beta emulators firestore start --project=test-project &

    # Start Pub/Sub emulator
    print_message "Starting Pub/Sub emulator..."
    gcloud beta emulators pubsub start --project=test-project &

    print_message "Local emulators are running. Use 'gcloud beta emulators firestore stop' and 'gcloud beta emulators pubsub stop' to stop them."
fi

print_message "Setup complete! You can now start developing the GitHub Repository Scanner."

# HUMAN ASSISTANCE NEEDED
# The following steps may require manual intervention:
# 1. Update the .env file with actual values for API keys and project IDs.
# 2. Ensure that Google Cloud SDK is installed and configured correctly.
# 3. If using real Google Cloud services instead of emulators, update the necessary configuration files.