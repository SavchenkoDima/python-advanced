from flask_restful import Resource
from flask import request, jsonify
from models.workers import Person
from schems.workers_schema import PersonSchema
from pprint import pprint as pp

from marshmallow import ValidationError


class WorkerResurse(Resource):

    def get(self, id=None):
        if not id:
            objects = Person.objects
            return PersonSchema().dump(objects, many=True)
        return PersonSchema().dump(Person.objects(id=id).get())

    def post(self):
        print('1')
        schema = PersonSchema()
        try:
            resul = schema.load(request.json)
        except ValidationError as err:
            print(err.messages)
            print(err.valid_data)
            return err.messages

        error = PersonSchema().validate(request.json)
        if error:
            return error
        obj = Person(**request.json).save()
        return PersonSchema().dump(Person.objects(id=obj.id).get())


    def put(self, id):
        obj = Person.objects(id=id).get()
        obj.update(**request.json)
        return PersonSchema().dump(obj.reload())

    def delete(self, id):
        obj = Person.objects(id=id).delete()
        if obj == 1:
            return jsonify(**{'delete': 'ok'})
        else:
            return jsonify(**{'delete': 'Error'})
