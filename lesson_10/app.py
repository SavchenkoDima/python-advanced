from flask import Flask, request, Response
# from models.workers import Person
# from schems.workers_schema import PersonSchema
from flask_restful import Api
from resousers.worker_resourser import WorkerResurse
from flask import render_template

app = Flask(__name__)
api = Api(app)

api.add_resource(WorkerResurse, '/workers/', '/workers/<string:id>')


@app.route('/index')
def index():
    return render_template("index.html")


"""
set FLASK_DEBUG=1
flask run
"""

# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'GET':
#         obj = Person.objects.get()
#         return PersonSchema().dump(obj, many=True)
#     else:
#         validaty = PersonSchema().validate(**request.json)
#         if validaty:
#             return validaty
#         Person(**request.json).save()
#         return Response(status=201)


if __name__ == '__main__':
    app.run(debug=True)
