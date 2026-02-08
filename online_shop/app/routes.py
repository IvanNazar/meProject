from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product

# Define Blueprint
bp = Blueprint('routes', __name__)

# Define route for the home page
@bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html',
                           products=products)

@bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('product_list.html',
                           products=products)



@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name=request.form['name']
        price=request.form['price']
        product=Product(name=name, pricename=float(price))
        db.session.add(product)
        db.session.commit()
        flash("Product added")
        return redirect(url_for('routes.products'))
    return render_template('product_form.html', action='Add', product=None)

@bp.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted!')
    return redirect(url_for('routes.products'))

@bp.route('/update/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.description = request.form.get('description')
    
        print (f'''name={product.name}, price={product.price}, description={product.description}, stock={product.stock}, is_active={product.is_active}, category={product.category}, rating={product.rating}, sale={product.sale}''')
    
        db.session.commit()
        flash('Всё ок обнова прошла')

    return render_template('product_form.html', action='Update', product=product)