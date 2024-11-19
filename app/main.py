from fastapi import FastAPI
from . import models
from .database import engine
from .routes import order

app = FastAPI()

app.include_router(order.router)


models.Base.metadata.create_all(bind=engine)




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