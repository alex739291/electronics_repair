from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from models.client import Ticket
from schemas.ticket_schema import TicketCreate, TicketResponse

# Создаем роутер, все маршруты здесь будут автоматически начинаться с /tickets
router = APIRouter(prefix="/tickets", tags=["Tickets"])
@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
async def create_ticket(ticket: TicketCreate, db: AsyncSession = Depends(get_db)):
    new_ticket = Ticket(**ticket.model_dump())
    
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    
    return new_ticket

@router.get("/", response_model=list[TicketResponse])
async def get_tickets(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Ticket))
    tickets = result.scalars().all()
    return tickets    