from mongoengine import *

from models.models import Category, Product, Texts, Properties, Users

# product = Product.objects()

# for i in product:
#     print(i.id)
#     category_obj_db = Product.objects.get(id=i.id)
#     with open('imag.jpg', 'rb') as f:
#         category_obj_db.photo_product.put(f, collection_name='images/jpeg')
#         category_obj_db.save()



# product_dict = {
#     'title': 'SAMSUNG WW60J30G03WDUA',
#     'description': 'Габариты (ВхШхГ): 85x60x45 см',
#     'price': 11499,
#     'new_prise': 0,
#     'is_discount': False,
#     #'properties': True,
#     'category': category_obj_db
#}




# category_dict = {
#     'title': 'Measuring-technique',
#     'description': 'about Measuring-technique',
#     #'subcategory': ,
# }
# new_cat = Category(**category_dict)
# new_cat.save()

product = Product.objects.get(id='5dc7130ee5712505491e96bd')
user_obj = Users.objects.get(id='5dc7df24850aabc50a9dd346')

user_obj.add_product(product)
user_obj.save()

