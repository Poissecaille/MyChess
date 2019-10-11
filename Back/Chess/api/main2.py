from flask import request
from flask_restful import Resource

from Chess.managers.products import search_products, get_product_by_name, delete_product, update_product, add_new_product

class Products(Resource):
    def get(self):
        query = request.args['query']
        products_matching = search_products(query, category=None) #a revoir
        products = [product.get_small_data() for product in products_matching]
        return products
    def post(self):
        data = request.json
        product =add_new_product(data['name'],data['price'],data['dimension'],data['material'],data['category'])
        return product.get_small_data()

class Product(Resource):
    def get(self, product_name):
        product = get_product_by_name(product_name)
        return product.get_small_data()
    def patch (self,product_name):
        data=request.json
        update_product(product_name,data['material'],data['category'])
    def delete(self, product_name):
        result = delete_product(product_name)
        return result

class Price(Resource):
    def get(self):
        prices=[]
        variable = Price.select()
        for price in variable:
            prices.append(price.name)
        return prices

class Dimension(Resource):
    def get(self):
        dimensions=[]
        variable = Dimension.select()
        for dimension in variable:
            dimensions.append(dimension.name)
        return dimensions

class Material(Resource):
    def get (self):
        materials = []
        variable = Material.select()
        for material in variable:
            materials.append(material.name)
        return materials

class Category(Resource):
    def get(self):
        categories = []
        variable = Category.select()
        for category in variable:
            categories.append(category.name)
        return categories
