from fastapi import APIRouter

from gym_tracker.app.api.v1 import users

api_router: APIRouter = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
