from fastapi import FastAPI
from .core.config import settings
from .users import routes as user_routes

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include routers
app.include_router(user_routes.router, prefix="/users", tags=["users"])
