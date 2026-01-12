from flask import Flask, jsonify, render_template, request, redirect, url_for
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

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        print(request.form)  

        slide = {
            "title": request.form.get("title"),
            "text": request.form.get("text"),
            "location": request.form.get("location"),
            "duration": int(request.form.get("duration", 8)),
            "active": True
        }

        slides_collection.insert_one(slide)
        return redirect(url_for("admin"))

    return render_template("admin.html")

@app.route("/admin/slides/<location>/deactivate")
def deactivate_slides(location):
    slides_collection.update_many(
        {"location": location},
        {"$set": {"active": False}}
    )
    return redirect(url_for("admin"))


if __name__ == "__main__":
    print("Flask wordt gestart")
    app.run(debug=True)
