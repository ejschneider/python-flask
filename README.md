# python-flask
  a simple python api used to create and manage stores as well as the item within them. base code generated from following udemy.com/course/rest-api-flask-and-python

  intended to be used with Atom and Postman ( https://www.postman.com/downloads/ ) for checking api endpoints and testing

# Getting started
# Initializing VM
  on the command line, navigate to the scripts folder and enter ' activate '. Should see (venv3.9) before the terminal to confirm it is working. make sure to open 
  atom after activating the virtual environment, or else the dependencies won't be found 
  
# Creating the database and Starting the server
  after activating the VM, navigate to code and enter ' atom . ' This will open atom with the codebase. There should be a sample database ' data.db ' in the folder.
  It is recommended to delete this file and let the application create the database from scratch. It is currently set up to only create the database after the first query.
  
  Simply run the code from the app.py file. This should start the development server at http://127.0.0.1:5000/ . Once the server is running, we can open Postman to
  check endpoints and manipulate our database
  
# Setting up Postman
  Open Postman and create a new Get request. In the request panel, type http://127.0.0.1:5000/items . This should return a list of all items 
  in our database (currently empty). Save this request as /items.
  
  In app.py, api.add_resource shows our list of all possible endpoints
  '/item/<string:name>'
  '/items'
  '/register'
  '/users'
  '/store/<string:name>'
  '/stores'
  
  We can create requests in Postman for each of these endpoints. Below is a list of all requests and their intended purpose:
  
  # ITEMS ENDPOINTS
  
  GET
  /items
  Should return a list of items , each in JSON format.
  
  
  DEL
  /items
  Deletes ALL items in ALL stores. Requires JWT
  
  
  GET
  /item/<name>
  Should return a specified item of type < name >. JWT required
  
  
  POST
  /item/<name>
  Adds an items to database with < name >, price, and in a store of store_id
  
  
  PUT
  /item/<name>
  This will create a new item of type < name >, or update an existing item of type < name >.
  
  
  DEL
  /item/<name>
  Removes an item of type < name >
  
  # USERS ENDPOINTS
  
  GET
  /users
  Returns a list of all users in database
  
  
  DEL
  /users
  Deletes ALL users in database. JWT required
  
  
  POST
  /auth
  Given a username and password that exists in database, returns a JWT token
  
  
  POST
  /register
  Adds a user to database with username and password
  
  
  DEL
  /register
  Deletes a user from the database
  
  # STORES ENDPOINTS
  
  GET
  /stores
  Returns a list of ALL stores and ALL items within each store
  
  
  DEL
  /stores
  Deletes ALL stores with no items from database. Stores with items remain intact. JWT required
  
  
  GET
  /store/<name>
  Returns a store of specified < name >, and all items within
  
  
  POST
  /store/<name>
  Creates a store with name < name >
  
  
  DEL
  /store/<name>
  Deletes store of type < name > with no items from database. Delete failed if items exist in store. JWT required
  
# Running Tests
