from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

class Users(Resource):
  # methods go here
  def get(self):
    data = pd.read_csv('users.csv')
    data = data.to_dict()
    return {'data': data}, 200

  def post(self):
    parser = reqparse.RequestParser()

    parser.add_argument('userId', required=True)
    parser.add_argument('name', required=True)
    parser.add_argument('city', required=True)

    args = parser.parse_args()

    # read the CSV file
    data = pd.read_csv('users.csv')

    if args['userId'] in list(data['userId']):
      return {
        'message': f"'{args['userId']}' already exists."
      }, 401
    else:
      new_data = pd.DataFrame({
        'userId': args['userId'],
        'name': args['name'],
        'city': args['city'],
        'locations': [[]]
      })
      data = data.append(new_data, ignore_index=True)
      data.to_csv('users.csv', index=False)
      return {'data': data.to_dict()}, 200

class Locations(Resource):
  # methods go here
  pass

app = Flask(__name__)
api = Api(app)
api.add_resource(Users, '/users') # '/users' is our entry point
api.add_resource(Locations, '/locations') # '/locations' is our entry point

if __name__ == "__main__":  
  app.run() # run the Flask App