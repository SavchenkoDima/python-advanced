from models.models import Category, Product, Texts

#category_obj = Category('computers-notebooks')
#category_obj_db = Category.objects.get(name_category='vegetables')
#print(category_obj_db)

product_dict = {
    'name_product': 'tomato',
    'quantity': 200,
    'price': 15.50,
    'product_for_sale': True,
    #'category': category_obj_db
}
#product_obj = Product(**product_dict)
#product_obj.save()

category_dict = {
    'title': 'Measuring-technique',
    'description': 'about Measuring-technique',
    #'subcategory': ,
}
# new_cat = Category(**category_dict)
# new_cat.save()
# sub_category = Category.objects.get(title='Measuring-technique')
# category_obj = Category.objects.get(title='Instruments')
#
# category_obj.add_subcategory(sub_category)
# category_obj.save()

text_dict = {
    'title': 'contacts',
    'body': """
    г. Киев, пр. С. Бандеры, 6

г. Киев, ул. Крещатик, 20-22

г. Киев, ул. Киото, 25

г. Киев, пр. Победы, 24

г. Киев, ул. Декабристов, 9е

г. Киев, ул. М. Гришко, 3А

г. Одесса, ул. Академика Сахарова, 1б

г. Одесса, ул. Ивана и Юрия Лип (Гайдара), 13а

г. Одесса, пер. Семафорный, 4т
    """
}
new_text = Texts(**text_dict)
new_text.save()

