from flask import Flask, request
from flask_restful import Api, Resource

# create app & wrap it in an api
app = Flask(__name__)
api = Api(app)

# ! EXAMPLE

# dummy json
# names = {
#     "tim": {
#         "age": 19,
#         "gender": "male"
#     },
#     "lou": {
#         "age": 25,
#         "gender": "male"
#     }
# }

# # HelloWorld inherits from Resource class
# class HelloWorld(Resource):

#     # handles get method
#     def get(self, user_name):
#         return names[user_name]

#     def post(self):
#         return {"data": "POST to /helloworld!"}

# # register HelloWorld resource with the api
# # <type: var_name> is the syntax for url params
# api.add_resource(HelloWorld, "/helloworld/<string:user_name>")

# ! END EXAMPLE


videos = {
    "123": {
        "likes": 50
    }
}

class Video(Resource):
    def get(self, video_id):
        return videos[str(video_id)]

    # FIXME: should actually be a post method 
    def put(self, video_id):
        print(request.form["likes"])
        return videos[str(video_id)]


api.add_resource(Video, "/videos/<int:video_id>")

# start app in debug mode (NOT for production environment)
if __name__ == '__main__':
    app.run(debug=True)