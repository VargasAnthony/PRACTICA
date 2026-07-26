from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    tareas = relationship("Tarea", back_populates="owner")

class Tarea(Base):
    __tablename__ = "Tareas"

    id = Column(Integer, primary_key=True, index = True)
    titulo = Column(String, nullable = False)
    description = Column(String, nullable = True)
    completada = Column(Boolean, default = False)
    usuario_id = Column(ForeignKey("Usuarios.id"), nullable = False)

    owner = relationship("Usuario", back_populates="tareas")