from pymongo import MongoClient

try:
    conn = MongoClient("localhost", 27017)
    print("Connected successfully!")
except Exception as e:
    print("Could not connect to MongoDB:", e)

db = conn["mydatabase"]

collection = db["myTable"]
for record in collection.find():
    print(record)

