import unittest
from unittest.mock import patch, MagicMock
from google.cloud.scheduler_v1.types import Job
from backend.app.tasks.scheduler import schedule_weekly_scan, delete_scheduled_job

class TestTaskScheduler(unittest.TestCase):
    @patch('backend.app.tasks.scheduler.CloudSchedulerClient')
    def test_schedule_weekly_scan(self, mock_scheduler_client):
        # Arrange
        mock_client = MagicMock()
        mock_scheduler_client.return_value = mock_client
        mock_client.create_job.return_value = Job(name="projects/test-project/jobs/test-job")

        # Act
        result = schedule_weekly_scan("test-job", "0 0 * * 0")

        # Assert
        self.assertIsInstance(result, Job)
        self.assertEqual(result.name, "projects/test-project/jobs/test-job")
        mock_client.create_job.assert_called_once()

    @patch('backend.app.tasks.scheduler.CloudSchedulerClient')
    def test_delete_scheduled_job(self, mock_scheduler_client):
        # Arrange
        mock_client = MagicMock()
        mock_scheduler_client.return_value = mock_client

        # Act
        delete_scheduled_job("test-job")

        # Assert
        mock_client.delete_job.assert_called_once_with(name="test-job")

    @patch('backend.app.tasks.scheduler.CloudSchedulerClient')
    def test_schedule_weekly_scan_update_existing_job(self, mock_scheduler_client):
        # Arrange
        mock_client = MagicMock()
        mock_scheduler_client.return_value = mock_client
        mock_client.create_job.side_effect = Exception("Job already exists")
        mock_client.update_job.return_value = Job(name="projects/test-project/jobs/test-job")

        # Act
        result = schedule_weekly_scan("test-job", "0 0 * * 0")

        # Assert
        self.assertIsInstance(result, Job)
        self.assertEqual(result.name, "projects/test-project/jobs/test-job")
        mock_client.create_job.assert_called_once()
        mock_client.update_job.assert_called_once()

    @patch('backend.app.tasks.scheduler.CloudSchedulerClient')
    def test_delete_scheduled_job_not_found(self, mock_scheduler_client):
        # Arrange
        mock_client = MagicMock()
        mock_scheduler_client.return_value = mock_client
        mock_client.delete_job.side_effect = Exception("Job not found")

        # Act & Assert
        with self.assertRaises(Exception):
            delete_scheduled_job("non-existent-job")

    # HUMAN ASSISTANCE NEEDED
    # The following test case might need adjustments based on the actual implementation of error handling in the scheduler module
    @patch('backend.app.tasks.scheduler.CloudSchedulerClient')
    def test_schedule_weekly_scan_error_handling(self, mock_scheduler_client):
        # Arrange
        mock_client = MagicMock()
        mock_scheduler_client.return_value = mock_client
        mock_client.create_job.side_effect = Exception("Unexpected error")

        # Act & Assert
        with self.assertRaises(Exception):
            schedule_weekly_scan("test-job", "0 0 * * 0")

if __name__ == '__main__':
    unittest.main()