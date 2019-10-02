from peewee import *

from .database import db

class Product(Model):
    id = PrimaryKeyField()
    name = CharField()
    description = CharField()
    price = FloatField()
    material = FloatField()
    category = CharField()
    url=CharField()

    class Meta:
        database = db
        schema = 'public'

with db:
    Product.create_table(fail_silently=True)



class Category(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db
        schema = 'public'



class ProductCategory(Model): #classe héritée#distinction vente pièce/échiquier/ensemble
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='category')
    category = ForeignKeyField(Category, backref='products')

    class Meta:
        database = db
        schema = 'public'

with db:
    Category.create_table(fail_silently=True)
    ProductCategory.create_table(fail_silently=True)
