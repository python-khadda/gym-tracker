from fastapi import APIRouter

from gym_tracker.app.api.v1 import auth

api_router: APIRouter = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
