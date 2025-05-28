from typing import Generic,TypeVar,Optional
from abc import ABC
from generics.Identity import Identity

T = TypeVar('T')

class Entity(Generic[T],ABC):    
    def __init__(self,properties:T,id:Optional[Identity]=None):
        self.__id = id or Identity()
        self.__properties = properties
        
    @property
    def id(self)-> Identity:
        return self.__id
    
    @property
    def properties(self)-> T:
        return self.__properties
    
    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.id == other.id    