from typing import Type, TypeVar
from interfaces import IService
from repositories.base_repository import BaseRepository

T = TypeVar('T')
class BaseService(IService):
    app_config = {}
    def __init__(self):
        self._repositories = {}

    def _get_repository(self, repo_type:Type[T]) -> T:
        """Returns a singleton instance of the given repository type."""
        # Ensure the type is a subclass of BaseRepository
        if not issubclass(repo_type, BaseRepository):
            raise TypeError(f"{repo_type.__name__} is not a subclass of BaseRepository")
        
        # Create and cache the repository instance
        if repo_type not in self._repositories:
            self._repositories[repo_type] = repo_type(self)
        return self._repositories[repo_type]
    
_services = {}
S = TypeVar('S', bound=IService)
def get_service(service_type: Type[S]) -> S:
    """Returns a singleton instance of the given repository type."""
    # Ensure the type is a subclass of IService
    if not issubclass(service_type, IService):
        raise TypeError(f"{service_type.__name__} is not a subclass of IService")
    
    # Create and cache the service instance
    if service_type not in _services:
        _services[service_type] = service_type()
    return _services[service_type]
    