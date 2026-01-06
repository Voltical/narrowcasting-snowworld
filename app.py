from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

print("app.py gestart")

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

print("MONGO_URI gevonden:", bool(MONGO_URI))
print("MONGO_DB:", MONGO_DB)

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[MONGO_DB]
slides_collection = db["slides"]

@app.route("/")
def home():
    return "Flask werkt!"

@app.route("/add-slide")
def add_slide():
    slide = {
        "title": "Welkom bij SnowWorld!",
        "text": "Veel plezier op de piste!",
        "location": "entree",
        "duration": 8,
        "active": True
    }
    slides_collection.insert_one(slide)
    return "Slide toegevoegd"

@app.route("/api/slides/<location>")
def get_slides(location):
    slides = list(slides_collection.find(
        {"location": location, "active": True},
        {"_id": 0}
    ))
    return jsonify(slides)



if __name__ == "__main__":
    print("Flask wordt gestart")
    app.run(debug=True)
