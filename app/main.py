from fastapi import FastAPI
from .database import Base, engine
from .routers import users, tasks

app = FastAPI(
    title="Mi API con FastAPI",
    description="API inicial para la primera prueba real",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"mensaje": "¡Servidor FastAPI corriendo con éxito!"}