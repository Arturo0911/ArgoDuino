from app import app
from flask import jsonify


@app.route("/", methods=["GET"])
def home():
    jsonify({
        "message": "Working"
    })