from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import signup
from db.session import engine
from db.base import Base

app = FastAPI(title="FastAPI Authentication v1.0.0")

# Enable CORS for frontend (React runs on port 3000 by default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allow all (GET, POST, OPTIONS, PUT, DELETE)
    allow_headers=["*"],  # allow all headers
)

# Create all tables at startup (development only)
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(signup.router, prefix="/api/v1/signup", tags=["signup"])
# app.include_router(login.router, prefix="/api/v1/login", tags=["login"])
