from fastapi import APIRouter, Depends
from backend.app.services.email_service import EmailService

router = APIRouter()

@router.post('/notifications')
async def send_email_notification(email_service: EmailService = Depends(), report_id: str = None):
    # HUMAN ASSISTANCE NEEDED
    # The confidence level for this function is below 0.8, indicating that some aspects may need review or improvement.
    # Consider adding error handling, input validation, and more detailed logging.

    try:
        # Call the EmailService to send the email with the report attached
        status = await email_service.send_email_with_report(report_id)
        
        # Return the status of the email notification
        return {"status": status}
    except Exception as e:
        # Log the error and return an appropriate error response
        # Implement proper error logging mechanism
        return {"status": "error", "message": str(e)}

# Additional endpoint for checking notification status could be added here
