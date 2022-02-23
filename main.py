from flask import Flask 
from flask_restful import Api, Resource

# create app & wrap it in an api
app = Flask(__name__)
api = Api(app)

# start app in debug mode (NOT for production environment)
if __name__ == '__main__':
    app.run(debug=True)