from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.repositories import router as repositories_router
from backend.app.api.reports import router as reports_router
from backend.app.api.notifications import router as notifications_router
from backend.app.core.logger import setup_logger
from backend.app.core.config import Settings

app = FastAPI()
settings = Settings()

def create_app() -> FastAPI:
    # Initialize the FastAPI application
    app = FastAPI()

    # Set up CORS middleware
    add_cors_middleware(app)

    # Include API routers
    app.include_router(repositories_router, prefix="/api")
    app.include_router(reports_router, prefix="/api")
    app.include_router(notifications_router, prefix="/api")

    # Configure logging
    setup_logger()

    return app

def add_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

# HUMAN ASSISTANCE NEEDED
# The following block might need adjustments based on how the application is run:
if __name__ == "__main__":
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)