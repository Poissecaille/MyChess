import click

from managers import products


@click.group()
def cli():
    click.echo('## Mychess ##')


@cli.group()
def load():
    pass

@load.command('datafile')
@click.argument('name')
def load_file(name):
    products.loadfiledata(name)

@cli.group()
def get():
    pass

@get.command('product')
@click.argument('name')
# @click.option('--abilities', is_flag=True)
# @click.option('--types', is_flag=True)
def get_name(name):
     product = products.get_product_by_name(name) #we call the manager
     click.echo(f'Product {product.name}')
     click.echo(f'Price: {product.price}')
     click.echo(f'Dimension:{product.dimension}')
     click.echo(f'Material:{product.material}')
     click.echo(f'Category:{product.category}') #ok?

@get.command('products')

@click.option('--price')
@click.option('--dimension')
@click.option('--material')
@click.option('--category')

def get_products(price, dimension, material, category):
    if price is not None:
        products_with_price = products.get_products_by_price(float(price))
        names = [p.name for p in products_with_price]
        click.echo(f'Products : {names}')
    if dimension is not None:
        products_with_dimension = products.get_products_by_dimension(float(dimension))
        names = [product.name for product in products_with_dimension]
        click.echo(f'Products:{names}')
    if material is not None:
        products_with_material = products.get_products_by_material(material)
        names = [product.name for product in products_with_material]
        click.echo(f'Products:{names}')
    if category is not None:
        products_with_category = products.get_products_by_category(category)
        names = [p.name for p in products_with_category]
        click.echo(f'Products : {names}')

@cli.group()
def add():
    pass


@add.command('product')
@click.argument('name')
@click.argument('price')
@click.argument('category')
@click.argument('dimension')
@click.argument('material')

def add_product(name, price,dimension, material,category):
    product=products.add_new_product(name, price, dimension,material, category)
    click.echo(f"{product.name} added to database")

@cli.group()
def search():
    pass


@search.command('products')
@click.argument('query')
def search_products(query):
    products_matching = products.search_products(query)
    names = [product.name for product in products_matching]
    click.echo(f'Products found: {names}')

