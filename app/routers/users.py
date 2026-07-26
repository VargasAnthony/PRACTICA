from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UsuarioBase, UsuarioCreate, UsuarioResponse, TareaBase, TareaCreate, TareaResponse
from database import get_db
from auth import hash_password, verify_password, create_acces_token, verify_access_token
from models import Usuario

router = APIRouter()

nuevo_objeto = 

@router.post("/register", response_model=UsuarioResponse)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="El Email ya esta registrado")
    hashed_pw = hash_password(usuario.password)

    usuario_nuevo = Usuario(email = usuario.email, hashed_password = hashed_pw)

    db.add(usuario_nuevo)     
    db.commit()               
    db.refresh(usuario_nuevo) 

    return usuario_nuevo