from pymongo import MongoClient
client=MongoClient()

client = MongoClient("mongodb://localhost:27017/")

mydb = client["my_database"]
mycollection = mydb["myTable"]

record = {
    "title": 'MongoDB and Python', 
    "description": 'MongoDB is no SQL database', 
    "tags": ['mongodb', 'database', 'NoSQL'], 
    "viewers": 104 
}

rec = mydb.myTable.insert(record)


# Find documents with specific criteria
for i in mycollection.find({"title": "MongoDB and Python"}):
      print(i)

# Count documents matching criteria
count = mycollection.count_documents({"title": "MongoDB and Python"})
print(count)