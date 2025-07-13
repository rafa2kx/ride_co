from abc import abstractmethod
from typing import Type, TypeVar

T = TypeVar('T')
class IService:
    @abstractmethod
    def _get_repository(self, repo_type:Type[T]) -> T:
        pass