from app.service_calls import get_product_data, get_component_data, update_components
from app.schemas import CheckAvailabilityRequest, CheckAvailabilityResponse
from fastapi import HTTPException


async def check_availability(request: CheckAvailabilityRequest):
    product_data = await get_product_data()
    component_data = await get_component_data()

    product_map = {prod["productId"]: prod for prod in product_data}

    response = []
    for item in request:
        product = product_map.get(item.productId)
        if not product:
            raise HTTPException(status_code=400, detail=f"Product {item.productId} not found.")

        components_needed = product["components"]
        max_count = min(
            component_data[comp["name"]] // comp["quantity"]
            for comp in components_needed
        )
        response.append({
            "productId": item.productId,
            "productName": product["name"],
            "availableCount": min(item.count, max_count)
        })
        for comp in components_needed:
            component_data[comp["name"]] -= comp["quantity"] * min(item.count, max_count)

    return response


async def produce_items(request):
    product_data = await get_product_data()
    component_data = await get_component_data()

    product_map = {prod["productId"]: prod for prod in product_data}

    for item in request:
        product = product_map.get(item.productId)
        if not product:
            raise HTTPException(status_code=400, detail=f"Product {item.productId} not found.")

        components_needed = product["components"]
        for comp in components_needed:
            total_needed = comp["quantity"] * item.count
            if component_data[comp["name"]] < total_needed:
                raise HTTPException(
                    status_code=400,
                    detail=f"Not enough {comp['name']} for {item.productId}."
                )

        for comp in components_needed:
            component_data[comp["name"]] -= comp["quantity"] * item.count

    await update_components(component_data)