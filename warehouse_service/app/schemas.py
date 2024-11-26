from pydantic import BaseModel

class ComponentIn(BaseModel):
    name: str
    quantity: int

class ComponentOut(ComponentIn):
    id: int

    class Config:
        orm_mode = True