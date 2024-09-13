import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.services.github_service import GitHubService
from backend.app.services.report_service import ReportService
from backend.app.services.email_service import EmailService
from unittest.mock import Mock, patch

client = TestClient(app)

@pytest.fixture
def mock_github_service():
    return Mock(spec=GitHubService)

@pytest.fixture
def mock_report_service():
    return Mock(spec=ReportService)

@pytest.fixture
def mock_email_service():
    return Mock(spec=EmailService)

def test_get_top_repositories(mock_github_service):
    mock_repositories = [
        {"name": "repo1", "owner": "owner1", "url": "url1", "stars_gained": 100, "total_stars": 1000},
        {"name": "repo2", "owner": "owner2", "url": "url2", "stars_gained": 200, "total_stars": 2000},
    ]
    mock_github_service.fetch_top_repositories.return_value = mock_repositories

    with patch("backend.app.api.repositories.GitHubService", return_value=mock_github_service):
        response = client.get("/repositories")

    assert response.status_code == 200
    assert response.json() == mock_repositories

def test_generate_report(mock_report_service):
    mock_report_url = "https://storage.googleapis.com/reports/report123.csv"
    mock_report_service.generate_csv_report.return_value = mock_report_url

    with patch("backend.app.api.reports.ReportService", return_value=mock_report_service):
        response = client.post("/reports")

    assert response.status_code == 200
    assert response.json() == {"report_url": mock_report_url}

def test_get_report():
    mock_report_id = "report123"
    mock_report_url = "https://storage.googleapis.com/reports/report123.csv"

    with patch("backend.app.api.reports.get_report", return_value=mock_report_url):
        response = client.get(f"/reports/{mock_report_id}")

    assert response.status_code == 200
    assert response.json() == {"report_url": mock_report_url}

def test_send_email_notification(mock_email_service):
    mock_report_id = "report123"
    mock_email_status = "Email sent successfully"
    mock_email_service.send_email_with_report.return_value = mock_email_status

    with patch("backend.app.api.notifications.EmailService", return_value=mock_email_service):
        response = client.post("/notifications", json={"report_id": mock_report_id})

    assert response.status_code == 200
    assert response.json() == {"status": mock_email_status}

# HUMAN ASSISTANCE NEEDED
# The following test cases might need additional setup or mocking depending on the exact implementation of the endpoints:
# 1. Test error handling for each endpoint (e.g., invalid input, service unavailability)
# 2. Test pagination for the /repositories endpoint if implemented
# 3. Test authentication and authorization if implemented
# 4. Test rate limiting if implemented
