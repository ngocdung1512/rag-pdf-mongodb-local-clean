"""This script pings the MongoDB Database with the environemnt variables to test the connection"""

# Import thư viện cần thiết 
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
atlas_uri = getenv("ATLAS_URI")
mongodb_db = getenv("MONGODB_DB")
mongodb_collection = getenv("MONGODB_COLLECTION")

# Debug print statements | In ra 3 thông số trên để kiểm tra xem có bị thiếu/đặt sai biến không.
print(f"ATLAS_URI: {atlas_uri}")
print(f"MONGODB_DB: {mongodb_db}")
print(f"MONGODB_COLLECTION: {mongodb_collection}")

# Create MongoDB client
client = MongoClient(atlas_uri)         # kết nối Mongo Atlas theo URI
db = client[mongodb_db]                 # trỏ đến đúng database
collection = db[mongodb_collection]     # trỏ đến collection bên trong database đó

# Test MongoDB connection | Dùng lệnh ping (chuẩn của MongoDB) kiểm tra xem kết nối đến server có hoạt động 
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

