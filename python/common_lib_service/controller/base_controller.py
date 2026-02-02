from abc import ABC, abstractmethod

class BaseController(ABC):
    def __init__(self):
        self.logger = self.get_logger()

    def get_logger(self):
        # возврат общего логгера
        ...

    def format_response(self, data, status=200):
        return {"data": data, "status": status}