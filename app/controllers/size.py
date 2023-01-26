from ..repositories.managers import SizeManager, BaseManager
from .base import BaseController


class SizeController(BaseController):
    manager = SizeManager

    @classmethod
    def create_manager(cls) -> BaseManager:
        return SizeManager()

