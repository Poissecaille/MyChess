from peewee import *

from .database import db

class Product(Model):
    id = PrimaryKeyField()
    name = CharField()
    #description = CharField()
    price = FloatField()
    dimension = FloatField()
    material = CharField()
    category = CharField()
    url=CharField()

    class Meta:
        database = db
        schema = 'public'

    @property
    def get_material_name(self):
        names = []
        for product_material in self.material:
            names.append(product_material.material.name)
        return names
    def get_category_name(self):
        names = []
        for product_category in self.categories:
            names.append(product_category.category.name)
        return names

    def get_small_data(self):
         return {'name': self.name, 'price': self.price, 'dimension':self.dimension, 'material': self.get_material_name(), 'category': self.get_category_name()}# 'sprite_front': self.sprite_front}

with db:
    Product.create_table(fail_silently=True)

class Category(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db
        schema = 'public'

class Material(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db
        schema = 'public'

class Price(Model):
    id = PrimaryKeyField()
    name = FloatField()

    class Meta:
        database = db
        schema = 'public'


class Dimension(Model):
    id = PrimaryKeyField()
    name = FloatField()

    class Meta:
        database = db
        schema = 'public'

class ProductMaterial(Model):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='material')
    material = ForeignKeyField(Material,backref='products')

    class Meta:
        database = db
        schema = 'public'

with db:
    Material.create_table(fail_silently=True)
    ProductMaterial.create_table(fail_silently=True)

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

class ProductDimension(Model):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='dimension')
    material = ForeignKeyField(Dimension,backref='products')

    class Meta:
        database = db
        schema = 'public'

with db:
    Dimension.create_table(fail_silently=True)
    ProductDimension.create_table(fail_silently=True)

class ProductPrice(Model):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='material')
    price = ForeignKeyField(Price,backref='products')

    class Meta:
        database = db
        schema = 'public'

with db:
    Price.create_table(fail_silently=True)
    ProductPrice.create_table(fail_silently=True)