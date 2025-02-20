# API-CRUD
# API AdventureWorks

## Description
Cette API permet de gérer les produits de l'entreprise AdventureWorks. Elle permet de réaliser les opérations CRUD suivantes :
- Créer un produit
- Lire un produit
- Mettre à jour un produit
- Supprimer un produit

## Installation
1. Clonez ce repository.
2. Créez un environnement virtuel : `python -m venv venv`
3. Installez les dépendances : `pip install -r requirements.txt`
4. Lancez l'application : `uvicorn app.main:app --reload`

## Endpoints
### Liste des produits
- **URL :** `/products`
- **Méthode :** `GET`

### Détails d'un produit
- **URL :** `/products/{product_id}`
- **Méthode :** `GET`

### Créer un produit
- **URL :** `/products`
- **Méthode :** `POST`

### Mettre à jour un produit
- **URL :** `/products/{product_id}`
- **Méthode :** `PUT`

### Supprimer un produit
- **URL :** `/products/{product_id}`
- **Méthode :** `DELETE`
