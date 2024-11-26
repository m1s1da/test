from sqlalchemy.orm import Session
from .models import Component

def get_component(db: Session, name: str):
    return db.query(Component).filter(Component.name == name).first()

def update_component(db: Session, name: str, quantity: int):
    component = db.query(Component).filter(Component.name == name).first()
    if component:
        component.quantity = quantity
        db.commit()
        db.refresh(component)
        return component
    return None