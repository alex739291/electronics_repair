from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 1. Импортируем наш движок БД и базовый класс
from core.database import engine
from models.base import Base

# 2. ОЧЕНЬ ВАЖНО: Импортируем файл с моделями, чтобы SQLAlchemy о них узнала
import models.client 

from api.clients import router
from api.tickets import router as tickets_router
from api import about

# 3. Функция жизненного цикла (Lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Этот код выполняется один раз при старте сервера
    async with engine.begin() as conn:
        # Берем наши чертежи и строим по ним таблицы в PostgreSQL
        await conn.run_sync(Base.metadata.create_all)
    yield
    # (Всё, что после yield, выполняется при выключении сервера)

# 4. Передаем lifespan в главное приложение
app = FastAPI(title="Electronics Repair API", lifespan=lifespan)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
app.include_router(tickets_router)
app.include_router(about.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Electronics Repair API!"}