from sqlmodel import Field, SQLModel

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    stock: int
