from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Product:
    product_id: int
    name: str
    price: float
    description: str | None = None


# product = Product(product_id=1, name='Apple', price=1.0, description='Fresh Apple')


@dataclass(slots=True, kw_only=True)
class Order:
    order_id: int
    client_id: int
    total: float = field(init=False, default=0.0)
    products: List[Product] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        self.__calculate_total()

    def __calculate_total(self):
        self.total = sum([product.price for product in self.products])


p_apple = Product(product_id=1, name="Apple", price=2.0, description="Fresh Apple")

order = Order(order_id=1, client_id=1, products=[p_apple], created_at=datetime.now())

print(order)

print(asdict(order))
print(astuple(order))
