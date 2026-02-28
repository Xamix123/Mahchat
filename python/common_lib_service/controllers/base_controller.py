from abc import ABC
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class BaseController(ABC):
    def __init__(self):
        self.logger = self.get_logger()

    def get_logger(self):
        pass

    def success(self, data=None, status_code: int = 200):

        body = {
            "success": True,
            "data": jsonable_encoder(data) if data is not None else None,
        }

        return JSONResponse(status_code=status_code, content=body)

    def error(self, message: str, status_code: int = 400):

        body = {"success": False, "error": message}

        return JSONResponse(status_code=status_code, content=body)
