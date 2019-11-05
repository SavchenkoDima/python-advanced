from flask import Flask
from flask import render_template, request
from models.products import Product, Category

app = Flask(__name__)


@app.route('/admin/')
def admin():
    return render_template('admin.html')


@app.route('/admin/create-category/', methods=['POST', 'DELETE', 'GET'])
def add_category():
    if request.method == 'POST':
        new_name = request.form.get('name_category')
        category_obj = Category(new_name)
        category_obj.save()
        category_obj_db = Category.objects
        return render_template("category.html", data=category_obj_db)
    if request.method == 'GET':
        return render_template('add_category.html')


@app.route('/admin/create-product/', methods=['POST', 'GET', 'DELETE'])
def add_product():
    if request.method == 'POST':
        category_obj_db = Category.objects.get(name_category=request.form.get('category'))
        product_dict = {
            'name_product': request.form.get('name_product'),
            'quantity': request.form.get('quantity'),
            'price': request.form.get('price'),
            'product_for_sale': request.form.get('bool'),
            'category': category_obj_db
        }
        product_obj = Product(**product_dict)
        product_obj.save()
        category_obj_db = Category.objects
        return render_template("add_product.html", data=category_obj_db)
    if request.method == 'GET':
        category_obj_db = Category.objects
        return render_template('add_product.html', data=category_obj_db)


@app.route('/')
def category():
    category_obj_db = Category.objects
    return render_template("category.html", data=category_obj_db)


@app.route('/category/<string:id>')
def products(id):
    products_obj_db = Product.objects(category=id)
    return render_template("products.html", data=products_obj_db)


@app.route('/product/<string:id>')
def product(id):
    product_obj_db = Product.objects.get(id=id)
    return render_template("product.html", data=product_obj_db)


if __name__ == '__main__':
    app.run()

"""
set FLASK_DEBUG=1
flask run
"""
