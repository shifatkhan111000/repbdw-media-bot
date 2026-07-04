from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["repbdw_bot"]
movies = db["movies"]

print("✅ MongoDB Connected Successfully")

def add_movie(name, year, file_id):
    movies.insert_one({
        "name": name,
        "year": year,
        "file_id": file_id
    })

def get_movie(name):
    return movies.find_one({
        "name": {
            "$regex": f"^{name}$",
            "$options": "i"
        }
    })
def add_movie(name, year, file_id):
    movies.insert_one({
        "name": name,
        "year": year,
        "file_id": file_id
    })
