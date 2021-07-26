"""
Title: Assignment 9.3
Author: Professor Krasso
Date: 25 July 2021
Modified By: Angela Martin
Description: This program demonstrates the use of Python.
"""

# Imports
from pymongo import MongoClient
import pprint

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# Update one user in the users collection using the update_one() method
db.users.update_one(
    {"employee_id": "7744112"},
    {
        "$set": {
            "email": "angtmartin@my365.bellevue.edu"
        }
    }
)

# Query the users collection using find_one() method
pprint.pprint(db.users.find_one({"employee_id": "7744112"}))