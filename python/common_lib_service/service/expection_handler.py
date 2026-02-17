from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


class ExceptionHandler:

    @staticmethod
    async def handle_validation_exception(
        request: Request,
        exc: RequestValidationError
    ) -> JSONResponse:

        error = exc.errors()[0]

        field = error["loc"][-1]
        message = error["msg"]

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": f"{field}: {message}"
            }
        )


    @staticmethod
    async def handle_generic_exception(
        request: Request,
        exc: Exception
    ) -> JSONResponse:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "Internal server error"
            }
        )


    @staticmethod
    def register(app: FastAPI) -> None:

        app.add_exception_handler(
            RequestValidationError,
            ExceptionHandler.handle_validation_exception
        )

        app.add_exception_handler(
            Exception,
            ExceptionHandler.handle_generic_exception
        )
