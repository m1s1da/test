import httpx
from app.config import WAREHOUSE_API_URL, CATALOG_API_URL

async def get_product_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{CATALOG_API_URL}/products")
        response.raise_for_status()
        return response.json()

async def get_component_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{WAREHOUSE_API_URL}/components")
        response.raise_for_status()
        return response.json()

async def update_components(components: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{WAREHOUSE_API_URL}/components", json=components)
        response.raise_for_status()
