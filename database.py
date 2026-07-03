from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["repbdw_bot"]

movies = db["movies"]

print("✅ MongoDB Connected Successfully")
