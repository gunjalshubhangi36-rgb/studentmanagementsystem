from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("Mongodburl")

ConnectionString = MongoClient(url)

database = ConnectionString["StudentManagement11212"]

collection = database["STDCollection111223"]

# h6hwE57pvLwlcnhS
# mongodb+srv://Shubhangi:<db_password>@cluster0.a6gcai7.mongodb.net/?appName=Cluster0

# mongodb+srv://Shubhangi:<db_password>@test.0ro6rrk.mongodb.net/?appName=test
# ZhsaFt0BDz1zooNn