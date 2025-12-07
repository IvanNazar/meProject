from flask import Blueprint, render_template
from .models import db, Product

# Define Blueprint
bp = Blueprint('routes', __name__)

# Define route for the home page
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('product_list.html', products=products)