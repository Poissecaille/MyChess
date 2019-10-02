from peewee import *

from .database import db
from .product import Product

class Client(Model):
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    gender = CharField()
    age= IntegerField()
    mail=CharField()

    class Meta:
        database = db
        schema = 'public'

class Avis(Model):
    id=PrimaryKeyField()
    client=ForeignKeyField(Client,backref='avis_clients')
    product=ForeignKeyField(Product,backref='avis_produits')
    text=CharField()

    class Meta:
        database=db
        schema='public'

class Facture(Model):
    id = PrimaryKeyField()
    amount = FloatField()

    class Meta:
        database = db
        schema = 'public'

class Panier(Model):
    id=PrimaryKeyField()
    name=CharField()
    client=ForeignKeyField(Client,backref='panier_client')
    facture=ForeignKeyField(Facture,backref='amounts_panier')

    class Meta:
        database=db
        schema='public'

class PanierProduct(Model):
    id=PrimaryKeyField()
    number_of_products=IntegerField()
    product=ForeignKeyField(Product,backref='number_product')
    panier=ForeignKeyField(Panier,backref='number_panier')

    class Meta:
        database=db
        schema='public'

class Discount(Model):
    id=PrimaryKeyField()
    name=CharField()
    amount=FloatField()

    class Meta:
        database=db
        schema='public'

