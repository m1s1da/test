from fastapi import FastAPI, HTTPException
from app.schemas import CheckAvailabilityRequest, CheckAvailabilityResponse, ProduceItemsRequest
from app.logic import check_availability, produce_items
from app.errors import ErrorResponse

app = FastAPI()

@app.post("/calculator/api/checkAvailability", response_model=list[CheckAvailabilityResponse])
async def api_check_availability(request: CheckAvailabilityRequest):
    return await check_availability(request)

@app.post("/calculator/api/produceItems", response_model=None, responses={400: {"model": ErrorResponse}})
async def api_produce_items(request: ProduceItemsRequest):
    try:
        await produce_items(request)
        return {"status": "success"}
    except HTTPException as e:
        raise e
