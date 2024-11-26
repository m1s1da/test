from pydantic import BaseModel

class Product(BaseModel):
    productId: str
    count: int

class CheckAvailabilityRequest(list[Product]):
    pass

class CheckAvailabilityResponse(BaseModel):
    productId: str
    productName: str
    availableCount: int

class ProduceItemsRequest(list[Product]):
    pass
