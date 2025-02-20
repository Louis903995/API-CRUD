from fastapi import FastAPI
from app.routes.product import router as product_router
from app.security.auth import get_current_user

app = FastAPI(
    title="AdventureWorks API",
    description="API CRUD pour gérer les produits d'AdventureWorks",
    version="1.0.0",
)

# Ajouter le routeur pour les produits
app.include_router(product_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API AdventureWorks"}
