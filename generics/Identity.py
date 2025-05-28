import uuid
from typing import Optional

class Identity:       
    def __init__(self, value: Optional[str] = None):
        if not value:
            self.__value = str(uuid.uuid4())
        else:
            self.__value = value
        
    @property
    def value(self) -> str:
        return self.__value    
    
    def __eq__(self, other):
        if not isinstance(other, Identity):
            return False
        return self.value == other.value
    
    def __str__(self):
        return f"Identity(value={self.value})"
    
    def __repr__(self):
        return f"Identity(value={self.value})"
