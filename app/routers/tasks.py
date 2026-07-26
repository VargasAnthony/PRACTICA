from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import TareaBase, TareaCreate, TareaResponse
from database import get_db
from models import Usuario, Tarea
from dependencies import get_current_user


router = APIRouter()

@router.post("/tareas", response_model=TareaResponse)
def crear_tarea(tarea: TareaCreate, usuario_actual: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    tarea_nueva = Tarea(
    titulo = tarea.titulo,
    description = tarea.description,
    usuario_id = usuario_actual.id
    )

    db.add(tarea_nueva)     
    db.commit()               
    db.refresh(tarea_nueva) 

    return tarea_nueva