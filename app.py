import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    student = os.environ.get("STUDENT_NAME", "невідомий студент")
    return f"Hello from Render! Застосунок розгорнув: {student}"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)