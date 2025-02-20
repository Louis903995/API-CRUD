from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate
from app.db import session

router = APIRouter()

# Liste tous les produits
@router.get("/products", response_model=List[ProductOut])
async def list_products():
    products = session.query(Product).all()
    return products

# Détaille un produit par son ID
@router.get("/products/{product_id}", response_model=ProductOut)
async def get_product(product_id: int):
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Crée un nouveau produit
@router.post("/products", response_model=ProductOut, status_code=201)
async def create_product(product: ProductCreate):
    db_product = Product(**product.dict())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

# Met à jour un produit existant
@router.put("/products/{product_id}", response_model=ProductOut)
async def update_product(product_id: int, product: ProductUpdate):
    db_product = session.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    session.commit()
    session.refresh(db_product)
    return db_product

# Supprime un produit
@router.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int):
    db_product = session.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(db_product)
    session.commit()
    return {"message": "Product deleted successfully"}
