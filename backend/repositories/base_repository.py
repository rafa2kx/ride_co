from typing import TypeVar, Type
from interfaces import IService
from extension import db

T = TypeVar('T')
class BaseRepository:
    session = None
    def __init__(self, caller:IService):
        self.caller = caller
        self.session = db.session
    
    def _get_repository(self, repo_type:Type[T]) -> T:
        return self.caller._get_repository(repo_type)
    
    
    
