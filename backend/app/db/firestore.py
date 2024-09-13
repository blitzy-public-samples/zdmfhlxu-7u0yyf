from google.cloud.firestore import Client, DocumentReference, CollectionReference, DocumentSnapshot, Query
from backend.app.core.config import Settings

# Initialize Firestore client
db_client = Client()

def get_repository_collection() -> CollectionReference:
    """
    Retrieves the Firestore collection reference for repositories.

    Returns:
        CollectionReference: The Firestore collection reference for repositories.
    """
    return db_client.collection('repositories')

def get_repository_by_id(repository_id: str) -> DocumentSnapshot:
    """
    Fetches a repository document from Firestore by its ID.

    Args:
        repository_id (str): The ID of the repository to fetch.

    Returns:
        DocumentSnapshot: The Firestore document snapshot for the repository.
    """
    collection_ref = get_repository_collection()
    return collection_ref.document(repository_id).get()

def save_repository(repository_id: str, repository_data: dict) -> DocumentReference:
    """
    Saves or updates a repository document in Firestore.

    Args:
        repository_id (str): The ID of the repository to save or update.
        repository_data (dict): The data of the repository to save.

    Returns:
        DocumentReference: The Firestore document reference for the saved repository.
    """
    collection_ref = get_repository_collection()
    doc_ref = collection_ref.document(repository_id)
    doc_ref.set(repository_data, merge=True)
    return doc_ref

# HUMAN ASSISTANCE NEEDED
# The following functionality might be needed but is not explicitly specified in the requirements:
# - Querying repositories based on certain criteria (e.g., stars gained, total stars)
# - Deleting repositories
# - Batch operations for efficiency when dealing with multiple repositories
# Consider adding these functions if they are required for the application's functionality.
