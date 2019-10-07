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

    def get_material_name(self):
        names = []
        for product_material in self.material:
            names.append(product_material.material.name)
        return names

    # def get_small_data(self):
    #     return {'name': self.name, 'stats': self.stats, 'types': self.get_types_name(), 'sprite_front': self.sprite_front}


class Category(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db
        schema = 'public'

class Material(Model):
    id=PrimaryKeyField()
    name = CharField()

class ProductMaterial(Model):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='material')
    material = ForeignKeyField(Material,backref='products')

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
