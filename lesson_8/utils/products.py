from models.products import Product, Category

category_obj = Category('vegetables')
category_obj_db = Category.objects.get(name_category='vegetables')
print(category_obj_db)

product_dict = {
    'name_product': 'tomato',
    'quantity': 200,
    'price': 15.50,
    'product_for_sale': True,
    'category': category_obj_db
}

#category_obj.save()

product_obj = Product(**product_dict)
product_obj.save()
