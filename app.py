from flask import Flask, request

app = Flask(__name__)

reports = [{"name": "gg", "items": [{"name": "Chair", "price": 15.99}]}]

@app.get("/reports")
def get_reports():
    return {"reports": reports}

@app.post("/reports")
def create_report():
    request_data = request.get_json()

    new_store = {"name": request_data["name"], "items": []}
    reports.append(new_store)
    return reports, 201
@app.post("/reports/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for report in reports:
        if report["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            report["items"].append(new_item)
            return new_item, 201
    return {"msg": "report not found"}, 404

# @app.get("/store/<string:name>")
# def get_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return store
#     return {"message": "Store not found"}, 404
