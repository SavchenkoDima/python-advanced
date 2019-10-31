from flask_restful import Resource
from flask import request, jsonify
from models.workers import Person
from schems.workers_schema import PersonSchema


class WorkerResurse(Resource):

    def get(self, id=None):
        if not id:
            objects = Person.objects
            return PersonSchema().dump(objects, many=True)
        return PersonSchema().dump(Person.objects(id=id).get())

    def post(self):
        return jsonify(**{'method': 'post'})

    def put(self):
        return jsonify(**{'method': 'put'})

    def delete(self):
        return jsonify(**{'method': 'delete'})
