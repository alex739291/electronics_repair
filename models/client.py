import enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# 1. Importing Base from our neighboring file
from .base import Base

# 2. Defining the Enumeration for ticket statuses
class TicketStatus(enum.Enum):
    ACCEPTED = "accepted"
    IN_PROGRESS = "in_progress"
    WAITING_FOR_PARTS = "waiting_for_parts"
    DONE = "done"

# 3. Defining the Client model
class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone_number: Mapped[str]
    address: Mapped[str]
    
    # One-to-Many: One client has a list of tickets
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="client")

# 4. Defining the Ticket model
class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    
    # Target appliances: lavatrice, lavastoviglie, asciugatrice, etc.
    appliance: Mapped[str]       
    breakdown_type: Mapped[str]  
    
    status: Mapped[TicketStatus] = mapped_column(default=TicketStatus.ACCEPTED)
    
    # Many-to-One: Many tickets belong to one client
    client: Mapped["Client"] = relationship(back_populates="tickets")