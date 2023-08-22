from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return "APP WORKING!!!"


if __name__ == "__main__":
    app.run(debug=True)