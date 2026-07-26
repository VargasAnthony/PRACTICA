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


@router.get("/tareas", response_model=list[TareaResponse])
def listar_tareas(usuario_actual: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    tarea_db = db.query(Tarea).filter(Tarea.usuario_id == usuario_actual.id).all()

    return tarea_db

@router.put("/tareas/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(tarea_id: int, tarea_actualizada: TareaCreate, 
                    usuario_actual: Usuario = Depends(get_current_user), 
                    db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
    if tarea.usuario_id != usuario_actual.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso sobre esta tarea")
    tarea.titulo = tarea_actualizada.titulo
    tarea.description = tarea_actualizada.description

    db.commit()               
    db.refresh(tarea) 

    return tarea
