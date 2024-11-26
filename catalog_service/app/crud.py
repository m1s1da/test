from sqlalchemy.orm import Session
from .models import Product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def create_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product