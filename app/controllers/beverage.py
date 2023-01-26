from ..repositories.managers import BeverageManager, BaseManager
from .base import BaseController


class BeverageController(BaseController):

    @classmethod
    def create_manager(cls) -> BaseManager:
        return BeverageManager()

