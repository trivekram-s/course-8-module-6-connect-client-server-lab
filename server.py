from flask import Flask, jsonify, request
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
events=[{"id":1,"title":"Python Workshop"},{"id":2,"title":"Flask Meetup"}]
@app.route("/",methods=["GET"])
def home():
    return jsonify({"message":"Welcome to the Event Catalog API"}),200
@app.route("/events",methods=["GET"])
def get_events():
    return jsonify(events),200
@app.route("/events",methods=["POST"])
def add_event():
    data=request.get_json() or {}
    title=data.get("title")
    if not title:
        return jsonify({"error":"Title is required"}),400
    new={"id": max([e["id"] for e in events],default=0)+1,"title":title}
    events.append(new)
    return jsonify(new),201
if __name__=="__main__":
    app.run(debug=True)
