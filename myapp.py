#! usr/bin/env python3
print("go")
from flask import Flask,jsonify

app=Flask(__name__)


@app.route("/")
def index():
	return jsonify({"key1":1})

if __name__=="__main__":
	app.run(debug=True)
