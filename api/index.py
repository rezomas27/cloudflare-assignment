# api/index.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_headers():
    return request.headers

# Required for Vercel's handler
def handler(environ, start_response):
    return app(environ, start_response)
