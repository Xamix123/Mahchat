from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse


class ExceptionHandler:

    @staticmethod
    async def handle_generic_exception(
        request: Request, exc: Exception
    ) -> JSONResponse:

        return JSONResponse(
            status_code=500,
            content={"success": False, "error": "Internal server error"},
        )

    @staticmethod
    def register(app: FastAPI) -> None:

        app.add_exception_handler(Exception, ExceptionHandler.handle_generic_exception)
