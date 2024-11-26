from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    nails: int
    plywood: int
    boards: int


class ProductOut(ProductIn):
    id: int

    class Config:
        orm_mode = True
