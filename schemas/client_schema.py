from pydantic import BaseModel, ConfigDict

# Schema for incoming data (creating a client)
class ClientCreate(BaseModel):
    name: str
    phone_number: str
    address: str

# Schema for outgoing data (returning client info)
class ClientResponse(BaseModel):
    id: int
    name: str
    phone_number: str
    address: str
    
    # This allows Pydantic to read data directly from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)