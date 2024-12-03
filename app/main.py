from fastapi import FastAPI
from . import models
from .database import engine
from .routes import order,users,auth,foodlikes


app = FastAPI()




models.Base.metadata.create_all(bind=engine)

app.include_router(order.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(foodlikes.router)


@app.get("/")
def root():
    return {"message":"Hello World"}


# Sequel
# We're building a food order api 
# Users would be able to register, login and place an order as well as update the order 
# Users should also be able to delete the order 
# User can get all the orders and check if there's is there or get only their specific order
# List all order specific to a user
# Retrieve an order 

# So this is just a sample project to solify our knowledge of Fastapi
#  DB 
# We'd create 2 tables a. Order (name of order,published,created_at, id) and b. Users(name, email,password(for login), created at , id)
# Each order would be mapped to a user using our PK
# We're going to form a relationship between both tables so that each order would contain the user who ordered it.
# Authentication and validation as well as querying for orders as well.

# Implementation
# App folder - we'd have an app folder to contain our codes
# DB - We'd be using Postgress DB
# ROUTERS - our order,users, auth, oauth would all be routers and they'd be in our routes folder
# We'd provide authentication using Bearer token to validate each user we would also store our id in the token to know the current user who wants to access the order.
# We'd also provide shemas for validating data throughout our data lifecycle  as well as models for our sql We'd be incorporating alembic as well for db migration when we need to add changes.


# Deployment
# We'd deploy on Heroku and Ubuntu incorporating CI/CD for faster delivery 
# We'd containerze our api using Docker
# We'd write few tests to see our application passes this test.

# So let's dive in

# What i've done so far, created our db file and models as well, created our .env as well as our config file for our basesettings
# Created all the routes for our orders such as the get all orders, get one order, update order, delete order
# Created routes for user creation and hashed password so that it can be stored in the db
# Created routes for the user login via the OauthPassword request form, i also verifed that the entered password and the hashed_password are the same else we threw an error if they are not

# to do
# User login route as well as generating token on user login as well
# done with the login route where i used passwordauthform to get the username and password and then login the user, we also encode an access_token for the user and store the id in that token.
# We also have how we create the token, how we verify the token and extract as well as return the id, 
# We then use that id to retrieve the current user from the db and make it avaialable to any of our endpoint, we can also use this to protect our routes as well.

# What we want to implement
# setting up relationships between the tables, so we can query effectively. So we created a field called owner_id, this sets a link between the orders and users table, making sure that the users can order anything can we can keep track of which user has which order you get, so we can also protect some of our routes if we need users to filter based on if they are logged in or if their IDs correlate to the current_user which we're getting from the token which we embedded their id at 

# We also want to be able to delete and update oorders based on users, so user A would only be able to update Order B which he created and not order C which he didn't create, so that's what we mean when we protect our routes.

# We want to get the users who made a particular order and to do this we'd use relationships
# Setting a realtionship: it would tell SQL to fetch some data based off their relationships, so let's say we have our Orders if we want to get the Users who created this when we get the posts we'd need to use realtionships



# Query Parameters

# Limit to limit number of records returned, we can also use it for pagination
# skip which is offset , this is used to skip a specific number of records
# filter by using search to match desired query string
# % means space in your URL


# We wantt to create a table that then allows users to like a particular type of food, in this table it would be a composite primary key table in the sense that the two columns would be PKs right as well as one user can't like a type of food twice, so for example, User 1 can like any type of food but cannot like it more than once you get.

# This table is going to comprise of our user_id and our order_id


# We have to learn about joins in postgres because we'd have to join the orders and the foodlikes tables to get which user liked which order and we do this via joins


# So two things after solving this bug for over 30 minutes, a. the name of the column you're redefining let's say count(models.foodlike.order_id) must match what is in the pydantic model you're initiating 