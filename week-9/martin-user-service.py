"""
Title: Assignment 9.2
Author: Professor Krasso
Date: 25 July 2021
Modified By: Angela Martin
Description: This program demonstrates the use of Python.
"""

# Imports
from pymongo import MongoClient
import pprint
import datetime

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# Create new User
user = {
    "first_name": "Bob",
    "last_name": "Marley",
    "email": "bmarley@me.com",
    "employee_id": "7744112",
    "date_created": datetime.datetime.utcnow()
}

# Insert the new user document
user_id = db.users.insert_one(user).inserted_id

# Print the auto-generated user_id
print(user_id)

# Query the users collection using find_one() method
pprint.pprint(db.users.find_one({"employee_id": "7744112"}))