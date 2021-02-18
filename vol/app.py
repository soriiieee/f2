from flask import Flask, redirect, url_for , render_template
"""
https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=2
"""
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/content")
def user():
  return render_template("index.html", content= ["a","b","c"])


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)