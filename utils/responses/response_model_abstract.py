from abc import ABC, abstractmethod

class ResponseModelAbstract(ABC):
    @abstractmethod
    def set_response(self, response):
        pass