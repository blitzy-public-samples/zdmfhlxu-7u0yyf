from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from backend.app.services.github_service import GitHubService
from backend.app.schema.repository_schema import RepositorySchema

router = APIRouter()

@router.get('/repositories', response_model=List[RepositorySchema])
async def get_top_repositories(github_service: GitHubService = Depends(GitHubService)):
    # HUMAN ASSISTANCE NEEDED
    # The confidence level is 0.7, which is below the threshold of 0.8.
    # Additional implementation details or error handling might be required.
    
    # Call the GitHubService to fetch repository data
    repositories = await github_service.fetch_top_repositories(limit=500)
    
    # Process the data to filter the top 500 repositories
    # Note: Assuming the GitHubService already returns the top 500 repositories
    # If not, additional filtering logic should be implemented here
    
    # Convert the repository data to RepositorySchema objects
    repository_schemas = [RepositorySchema(**repo) for repo in repositories]
    
    return repository_schemas