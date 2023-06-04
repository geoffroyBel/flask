from flask import Flask, request

app = Flask(__name__)

reports = [{"name": "My reports", "items": [{"name": "Chair", "price": 15.99}]}]

@app.get("/reports")
def get_reports():
    return {"reports": reports}

@app.post("/reports")
def create_report():
    request_data = request.get_json()
    return {"reports": reports}
