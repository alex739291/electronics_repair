from pydantic import BaseModel, ConfigDict
from models.client import TicketStatus

# Схема для получения данных от пользователя (создание заявки)
class TicketCreate(BaseModel):
    client_id: int
    appliance: str
    breakdown_type: str

# Схема для отправки данных обратно пользователю
class TicketResponse(BaseModel):
    id: int
    client_id: int
    appliance: str
    breakdown_type: str
    status: TicketStatus
    
    model_config = ConfigDict(from_attributes=True)