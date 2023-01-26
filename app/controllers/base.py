from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import BaseManager


class BaseController:

    @classmethod
    def create_manager(cls) -> BaseManager:
        """Return a new manager object."""
        raise NotImplementedError("create_manager method not implemented.")

    @classmethod
    def get_by_id(cls, _id: Any) -> Tuple[Any, Optional[str]]:
        manager = cls.create_manager()
        try:
            return manager.get_by_id(_id), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_all(cls) -> Tuple[Any, Optional[str]]:
        manager = cls.create_manager()
        try:
            return manager.get_all(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def create(cls, entry: dict) -> Tuple[Any, Optional[str]]:
        manager = cls.create_manager()
        try:
            return manager.create(entry), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def update(cls, new_values: dict) -> Tuple[Any, Optional[str]]:
        manager = cls.create_manager()
        try:
            _id = new_values.pop('_id', None)
            if not _id:
                return None, 'Error: No id was provided for update'
            return manager.update(_id, new_values), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
