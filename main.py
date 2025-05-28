from entity.User import UserProps
from object_value.Email import Email
from object_value.CPF import CPF
from entity.User import User

novo_usuario = UserProps(
    name='Ewerton',
    email=Email('ewerton@email.com'),
    cpf=CPF('09253538414'),
    city='Patos-Pb'
)

cls_novo_usuario = User.create(novo_usuario)

print(cls_novo_usuario.id.value)
print(cls_novo_usuario.name)
print(cls_novo_usuario.email)
