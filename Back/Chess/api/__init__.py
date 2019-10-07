from flask import Blueprint
from flask_restful import Api #microservice get put delete restfull api

from Chess.models.database import db

from .main2 import Product, Products, Material, Category

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    api.add_resource(Products, '/products')
    api.add_resource(Product, '/product/<product_name>')
    api.add_resource(Material, '/material/<material>')
    api.add_resource(Category, '/category/<category>')
    app.register_blueprint(api_bp, url_prefix="/api/v1")