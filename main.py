from flask import Flask 
from flask_restful import Api, Resource

# create app & wrap it in an api
app = Flask(__name__)
api = Api(app)

# HelloWorld inherits from Resource class
class HelloWorld(Resource):

    # handles get method
    def get(self):
        return {"data": "GET to /helloworld"}

    def post(self):
        return {"data": "POST to /helloworld!"}

# register HelloWorld resource with the api
api.add_resource(HelloWorld, "/helloworld")

# start app in debug mode (NOT for production environment)
if __name__ == '__main__':
    app.run(debug=True)