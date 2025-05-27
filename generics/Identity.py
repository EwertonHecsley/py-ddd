import uuid

class Identity: 
    '''Identity class to represent a unique identifier.'''
      
    def __init__(self,value:str):
        if not value:
            self.__value = str(uuid.uuid4())
        self.__value = value
        
    @property
    def value(self)-> str:
        return self.__value    
    
    
    def __eq__(self, other):
        if not isinstance(other, Identity):
            return False
        return self.value == other.value
    
    def __str__(self):
        return f"Identity(value={self.value})"
    
    def __repr__(self):
        return f"Identity(value={self.value})"
        