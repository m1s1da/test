from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProductIn, ProductOut
from crud import get_product, get_all_products, create_product
from models import Product
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting catalog service...")
    yield
    print("Stopping catalog service...")


app = FastAPI(lifespan=lifespan)


@app.post("/products", response_model=ProductOut)
def add_product(product: ProductIn, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        nails=product.nails,
        plywood=product.plywood,
        boards=product.boards
    )
    return create_product(db, new_product)


@app.get("/products/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/products", response_model=list[ProductOut])
def read_all_products(db: Session = Depends(get_db)):
    return get_all_products(db)
