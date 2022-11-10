from models import Product, Category
from insert_data import add_category, add_product
from random import randint

query = Product.update(category_id = 5).where(Category.name=='кроссовки')
query.execute()

query = Product.update(price=(Product.))