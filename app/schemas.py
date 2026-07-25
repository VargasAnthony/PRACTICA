from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True


class TareaBase(BaseModel):
    titulo: str
    description: Optional[str] = None

class TareaCreate(TareaBase):
    pass

class TareaResponse(TareaBase):
    id: int
    usuario_id: int
    completada: bool

    class Config:
        from_attributes = True
