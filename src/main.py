from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import preguntas, jwt_auth_users, categorias, cuestionarios, usuarios

app = FastAPI()

app.include_router(preguntas.router)
app.include_router(jwt_auth_users.router)
app.include_router(categorias.router)
app.include_router(cuestionarios.router)
app.include_router(usuarios.router)
app.mount("/static",StaticFiles(directory="static"),name="static")