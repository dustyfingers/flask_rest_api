from flask import Flask 
from flask_restful import Api, Resource

# create app & wrap it in an api
app = Flask(__name__)
api = Api(app)

names = {
    "tim": {
        "age": 19,
        "gender": "male"
    },
    "lou": {
        "age": 25,
        "gender": "male"
    }
}

# HelloWorld inherits from Resource class
class HelloWorld(Resource):

    # handles get method
    def get(self, user_name):
        return names[user_name]

    def post(self):
        return {"data": "POST to /helloworld!"}

# register HelloWorld resource with the api
# <type: var_name> is the syntax for url params
api.add_resource(HelloWorld, "/helloworld/<string:user_name>")

# start app in debug mode (NOT for production environment)
if __name__ == '__main__':
    app.run(debug=True)