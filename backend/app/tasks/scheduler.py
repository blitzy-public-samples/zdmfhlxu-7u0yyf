from google.cloud.scheduler import CloudSchedulerClient
from google.cloud.scheduler_v1.types import Job
from google.protobuf.duration_pb2 import Duration
from backend.app.core.config import Settings
import logging

logger = logging.getLogger(__name__)

def schedule_weekly_scan(job_name: str, schedule_time: str) -> Job:
    """
    Schedules a weekly scan job using Google Cloud Scheduler.
    
    Args:
        job_name (str): The name of the job to be scheduled.
        schedule_time (str): The time at which the job should be scheduled (in cron format).
    
    Returns:
        Job: The created or updated Google Cloud Scheduler job.
    """
    try:
        client = CloudSchedulerClient()
        settings = Settings()
        
        # Create a job configuration
        job = Job(
            name=f"projects/{settings.FIRESTORE_PROJECT_ID}/locations/{settings.CLOUD_REGION}/jobs/{job_name}",
            schedule=schedule_time,
            time_zone="UTC",
            http_target={
                "uri": f"{settings.BACKEND_URL}/api/scan",
                "http_method": "POST",
            },
        )
        
        # Set the job to retry on failure
        job.retry_config = {
            "retry_count": 3,
            "max_retry_duration": Duration(seconds=300),
            "min_backoff_duration": Duration(seconds=30),
            "max_backoff_duration": Duration(seconds=300),
            "max_doublings": 5,
        }
        
        # Submit the job to Google Cloud Scheduler
        response = client.create_job(
            request={"parent": f"projects/{settings.FIRESTORE_PROJECT_ID}/locations/{settings.CLOUD_REGION}", "job": job}
        )
        
        logger.info(f"Job {job_name} scheduled successfully")
        return response
    except Exception as e:
        logger.error(f"Error scheduling job {job_name}: {str(e)}")
        raise

def delete_scheduled_job(job_name: str) -> None:
    """
    Deletes a scheduled job from Google Cloud Scheduler.
    
    Args:
        job_name (str): The name of the job to be deleted.
    """
    try:
        client = CloudSchedulerClient()
        settings = Settings()
        
        job_path = client.job_path(settings.FIRESTORE_PROJECT_ID, settings.CLOUD_REGION, job_name)
        client.delete_job(name=job_path)
        
        logger.info(f"Job {job_name} deleted successfully")
    except Exception as e:
        logger.error(f"Error deleting job {job_name}: {str(e)}")
        raise

# HUMAN ASSISTANCE NEEDED
# The following areas may need additional configuration or error handling:
# 1. Ensure that the Settings class in backend/app/core/config.py includes FIRESTORE_PROJECT_ID, CLOUD_REGION, and BACKEND_URL.
# 2. Implement proper error handling and retries for network-related issues.
# 3. Consider adding authentication to the HTTP target if required.
# 4. Verify that the /api/scan endpoint exists and can handle the weekly scan request.
