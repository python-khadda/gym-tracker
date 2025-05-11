from fastapi import Request
from fastapi.responses import JSONResponse

from gym_tracker.app.core.AppException import AppException
from gym_tracker.main import app


@app.exception_handler(AppException)
async def handle_app_exceptions(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
