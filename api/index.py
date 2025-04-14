# api/index.py
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_headers():
    return jsonify(dict(request.headers))

# 👇 This is the key line Vercel expects
vercel_handler = app
