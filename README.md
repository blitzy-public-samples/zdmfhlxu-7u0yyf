# GitHub Repository Scanner

## Introduction

The GitHub Repository Scanner is a powerful tool designed to track and analyze the popularity of GitHub repositories. It provides insights into repository trends by monitoring star counts and generating weekly reports. Key features include:

- Weekly scans of top GitHub repositories
- Tracking of star gain and total stars for each repository
- Generation of CSV reports with repository data
- Email notifications with attached reports
- User-friendly dashboard for visualizing trends

This application helps developers, project managers, and tech enthusiasts stay informed about the most popular and trending repositories on GitHub.

## System Requirements

To run the GitHub Repository Scanner, you'll need:

- Python 3.9 or higher
- Node.js 14 or higher
- Google Cloud account with the following services enabled:
  - Firestore
  - Cloud Storage
  - Cloud Scheduler
  - Cloud Run
- GitHub API access token

## Installation

Follow these steps to set up your development environment:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/github-repository-scanner.git
   cd github-repository-scanner
   ```

2. Set up the backend:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```
   cd ../frontend
   npm install
   ```

4. Configure environment variables:
   - Create a `.env` file in the `backend` directory with the following variables:
     ```
     GITHUB_API_KEY=your_github_api_key
     FIRESTORE_PROJECT_ID=your_firestore_project_id
     EMAIL_SENDER=your_email_sender
     EMAIL_RECIPIENT=your_email_recipient
     ```
   - Create a `.env` file in the `frontend` directory with:
     ```
     REACT_APP_API_URL=http://localhost:8000
     ```

5. Run the setup script:
   ```
   ./scripts/setup.sh
   ```

## Usage

To run the application locally:

1. Start the backend server:
   ```
   cd backend
   uvicorn app.main:app --reload
   ```

2. Start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Access the application at `http://localhost:3000`

To trigger a weekly scan manually:

python backend/app/tasks/weekly_scan.py
## Deployment

To deploy the application to Google Cloud:

1. Build Docker images:
   ```
   docker build -t gcr.io/your-project-id/github-scanner-backend:latest -f infrastructure/docker/Dockerfile.backend .
   docker build -t gcr.io/your-project-id/github-scanner-frontend:latest -f infrastructure/docker/Dockerfile.frontend .
   ```

2. Push images to Google Container Registry:
   ```
   docker push gcr.io/your-project-id/github-scanner-backend:latest
   docker push gcr.io/your-project-id/github-scanner-frontend:latest
   ```

3. Apply Terraform configurations:
   ```
   cd infrastructure/terraform
   terraform init
   terraform apply
   ```

4. Deploy services to Cloud Run:
   ```
   gcloud run deploy github-scanner-backend --image gcr.io/your-project-id/github-scanner-backend:latest --platform managed
   gcloud run deploy github-scanner-frontend --image gcr.io/your-project-id/github-scanner-frontend:latest --platform managed
   ```

Alternatively, you can use the deployment script:

./scripts/deploy.sh
## Contributing

We welcome contributions to the GitHub Repository Scanner! To contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive messages
4. Push your changes to your fork
5. Submit a pull request to the main repository

Please ensure your code adheres to our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.