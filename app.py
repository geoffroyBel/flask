from flask import Flask

app = Flask(__name__)

reports = [{"name": "My reports", "items": [{"name": "Chair", "price": 15.99}]}]

@app.get("/reports")
def get_reports():
    return {"reports": reports}
