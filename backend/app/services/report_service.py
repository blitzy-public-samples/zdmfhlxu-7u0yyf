from csv import writer
from io import StringIO
from backend.app.db.firestore import get_repository_collection
from google.cloud.storage import Client

storage_client = Client()

def generate_csv_report():
    # HUMAN ASSISTANCE NEEDED
    # The confidence level for this function is low (0.55). 
    # Please review and modify the implementation as needed.

    # Fetch the top 500 repositories from Firestore
    repo_collection = get_repository_collection()
    top_repos = repo_collection.order_by('stars_gained', direction='DESCENDING').limit(500).stream()

    # Generate CSV file
    csv_buffer = StringIO()
    csv_writer = writer(csv_buffer)
    
    # Write header
    csv_writer.writerow(['Name', 'Owner', 'URL', 'Stars Gained', 'Total Stars'])
    
    # Write repository data
    for repo in top_repos:
        repo_data = repo.to_dict()
        csv_writer.writerow([
            repo_data['name'],
            repo_data['owner'],
            repo_data['url'],
            repo_data['stars_gained'],
            repo_data['total_stars']
        ])

    # Upload CSV to Google Cloud Storage
    bucket_name = 'your-bucket-name'  # Replace with your actual bucket name
    blob_name = 'reports/top_500_repos.csv'
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    blob.upload_from_string(csv_buffer.getvalue(), content_type='text/csv')

    # Generate public URL
    url = blob.public_url

    return url

