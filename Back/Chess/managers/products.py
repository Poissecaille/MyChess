import requests
import csv
import re

from Chess.models.product import Product, ProductCategory, Category, ProductMaterial, Material
from Chess.models.client import Client


def get_product_by_name(name):
    product = Product.get(name=name)
    return product


def loadfiledata(name):
    with open(name, 'r') as f:
        reader=csv.DictReader(f)
        dict=[]
        for row in reader:
            print(row)

            name = row['name']
            name = re.sub(' ', '_', name)
            price = row['price']
            dimension = row['dimension']
            material = row['material']
            category = row['category']
            category = re.sub(' ', '_', category)
            print(name, price, dimension, material,category)

            add_new_product(name, price, dimension, material, category)

def get_products_by_price(min_price):
    results = []
    products = Product.select()
    for product in products:
        if product.price <= min_price:
            results.append(product)
    return results
def get_products_by_dimension(min_dimension):
    results = []
    products = Product.select()
    for product in products:
        if product.dimension <= min_dimension:
            results.append(product)
    return results

def get_products_by_material(material):
    material = []
    liste={1:'acajou et sycomore',2:'noyer',3:'sapele',4:'wengé',5:'ébène et érable',6:'saména de Guyane et buis',7:'albâtre et bois',8:'palissandre doré',9:'palissandre',10:'ébène',11:'0rose',12:'rose et ébène',13:'sheesha',14:'os',15:'ébène et buis',16:'bois'}
    for value in liste.values():
        material.append(value)
        print(material)

    # products = Product.select()
    # for product in products:
    #     sorted([i[:2] for i in liste])
    #     results.append(product)
    # return results
def get_products_by_category(category):
     results = []

     mycategory = Category.get(name=category)
     products = Product.select()
     for product in products:
         for a in product.category:
             if a.category == mycategory:
                results.append(product)
     return results

def create_product(name, material, category):
    stats = {'material': material, 'category': category}
    product = Product.get_or_none(name=name)
    if product is None:
        product = Product.create(name=name, **material, **category)
    else:
        product.update(**material, **category).execute()

    return product

def add_new_product(name, price, dimension, material,category): #if something is optional=>null
    """ create a new product in the database"""


    product=Product.get_or_none(name == name) # first name is class parameter, second is the name form the argument


    if product is None: #is None?
        product = Product.create(name=name, price=price, dimension=dimension, material=material, catergory=category)

    else: #the product already exit -> we update it

        ProductCategory.delete().where(ProductCategory.product == product).execute() # find the productcategory element associated with the product
        product.update(name=name, price=price, dimension=dimension, material=material, category=category)


    # correspond to the two options (if and else)
    query = Category.get_or_none(name=category)
    if query is None:
        query = Category.create(name=category)
    ProductCategory.create(product=product, category=query)  # join two table in another table

    return product

def delete_product(product_name):
    product = get_product_by_name((product_name))
    product.delete_instance(recursive=True) #???
    return True

def search_products(query,category):
    query = query.lower()
    products = Product.select().where(Product.name.contains(query))
    if category is not None:
        filtered_products=[]
        for product in products:
            categories=[]
            category_of_product=Product.select().where(ProductCategory.product==product)
            for product_category in category_of_product:
                category_name=product_category.category.name
                category.append(category_name)

            if category in categories:
                filtered_products.append(product)
        return filtered_products
    return products
#########################################################################################################
###########################################################################################################

def edit_pokemon_stats(name, material, category):
    """
    Edit stats of a product

    :param name:
    :param stat:
    :param new_value:
    :return:
    """
    product = get_product_by_name(name)

    update = {material:new_value,category:new_value2}
    product.update(
        **update).execute()  # update les stats pour tous les product bug a corriger, spécifier en fonction du nom du pkmn

    return product


def update_product(name, material, category):
    product = get_product_by_name(name)
    product.update(material).where(Product.name == name).execute()#
    product.update(category).where(Product.name == name).execute()#Les deux classes employées sont à revoir

    return product


def edit_product_material(name, material):
    product=get_product_by_name()
    ProductMaterial.delete().where(Product.name == name)
    for i, materials in enumerate(material):
        top = Material.get_or_none(name=materials)
        ProductMaterial.create(product=product, material=top, slot=i)  # a revoir
    return ProductMaterial

def delete_product(name):
    product = get_product_by_name(name)
    product.delete_instance(recursive=True)
    return True

