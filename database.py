from pymongo import MongoClient
from pymongo.errors import PyMongoError
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["repbdw_bot"]
movies = db["movies"]


def add_movie(name, year, file_id):
    try:
        movies.insert_one({
            "name": name,
            "year": year,
            "file_id": file_id
        })
        return True
    except PyMongoError as e:
        print("Add Movie Error:", e)
        return False


def get_movie(name):
    try:
        return movies.find_one({
            "name": {
                "$regex": f"^{name}$",
                "$options": "i"
            }
        })
    except PyMongoError as e:
        print("Search Error:", e)
        return None


def delete_movie(name):
    try:
        result = movies.delete_one({
            "name": {
                "$regex": f"^{name}$",
                "$options": "i"
            }
        })
        return result.deleted_count
    except PyMongoError as e:
        print("Delete Error:", e)
        return 0


def total_movies():
    return movies.count_documents({})
