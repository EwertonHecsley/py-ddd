from dataclasses import dataclass
from object_value import Email,CPF
from generics.Entity import Entity
from generics.Identity import Identity
from typing import Optional


@dataclass
class UserProps:
    name:str
    email:Email
    cpf:CPF
    city:str
    
    
class User(Entity):
    def __init__(self,properties:UserProps,id:Optional[Identity]=None):
        super().__init__(properties,id)
        
        
    @staticmethod
    def create(props: Optional[UserProps], id: Optional[Identity] = None) -> 'User':
        if props is None:
            raise ValueError("Propriedades obrigatórias não foram fornecidas.")
        if not props.name or not props.email or not props.cpf or not props.city:
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos.")
        return User(props, id)  
    
    @property
    def name(self) -> str:
        return self.properties.name
    
    @property
    def email(self) -> Email:
        return self.properties.email
    
    @property
    def cpf(self) -> CPF:
        return self.properties.cpf
    
    @property
    def city(self) -> str:
        return self.properties.city
    
    @name.setter
    def name(self, value: str):
        self.properties.name = value
        
    @email.setter
    def email(self, value: Email):
        self.properties.email = value
    
    @cpf.setter
    def cpf(self, value: CPF):
        self.properties.cpf = value
        
    @city.setter
    def city(self, value: str):
        self.properties.city = value            