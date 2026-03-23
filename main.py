from contextlib import asynccontextmanager
from fastapi import FastAPI

# 1. Импортируем наш движок БД и базовый класс
from core.database import engine
from models.base import Base

# 2. ОЧЕНЬ ВАЖНО: Импортируем файл с моделями, чтобы SQLAlchemy о них узнала
import models.client 

from api.clients import router
from api.tickets import router as tickets_router
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

app.include_router(router)
app.include_router(tickets_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Electronics Repair API!"}