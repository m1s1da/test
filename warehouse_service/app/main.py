from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import ComponentIn, ComponentOut
from .crud import get_component, update_component
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting warehouse service...")
    yield
    print("Stopping warehouse service...")

app = FastAPI(lifespan=lifespan)

@app.get("/components/{name}", response_model=ComponentOut)
def read_component(name: str, db: Session = Depends(get_db)):
    component = get_component(db, name)
    if component is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return component

@app.put("/components/{name}", response_model=ComponentOut)
def update_component_quantity(name: str, quantity: int, db: Session = Depends(get_db)):
    component = update_component(db, name, quantity)
    if component is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return component