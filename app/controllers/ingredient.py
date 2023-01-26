from ..repositories.managers import IngredientManager, BaseManager
from .base import BaseController


class IngredientController(BaseController):
    @classmethod
    def create_manager(cls) -> BaseManager:
        return IngredientManager()
