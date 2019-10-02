from flask import request
from flask_restful import Resource

from Chess.managers.products import search_products, get_product_by_name, delete_product


class Products(Resource):
    def get(self):
        query = request.args['query']
        products_matching = search_products(query, category=None) #a revoir
        products = [product.get_small_data() for product in products_matching]
        return products


class Product(Resource):
    def get(self, product_name):
        product = get_product_by_name(product_name)
        return product.get_small_data()
    def delete(self, product_name):
        result = delete_product(product_name)
        return result