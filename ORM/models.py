import peewee
from main import db
from  datetime import datetime


class Category(peewee.Model):
    category_id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=20, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())
    
    class Meta:
        database = db

class Product(peewee.Model):
    product_id = peewee.PrimaryKeyField(null=False)
    title =  peewee.CharField(max_length=20)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = peewee.ForeignKeyField(Category, to_field = 'category_id', on_delete = 'cascade', related_name='products')
    created_at = peewee.DateTimeField(default=datetime.now())
    class Meta:
        database = db
        db_table = 'products'
        order_by = ('created_at',)

db.connect()
# Category.create_table()
# Product.create_table()
