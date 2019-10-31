from models.workers import Person, Location

loctoion_obj = Location(street='KRe', city='Kiev')

person_dict = {
    'fist_name': 'Dima',
    'surname': 'Sav',
    'age': 23,
    'experiens': 25,
    'location': loctoion_obj
}

Person(**person_dict).save()
