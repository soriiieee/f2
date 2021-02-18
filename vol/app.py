import os,sys
cwd= os.getcwd()
sys.path.append("./tool")
sys.path.append("./py")
sys.path.append("/usr/local/lib/python3.8/dist-packages")
from get_snow import get_snow
from flask import Flask, redirect, url_for , render_template
import subprocess
"""
https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=2
"""

os.chdir(cwd)
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/map_amedas")
def map_amedas():
  return render_template("map_amedas.html")

@app.route("/snow/<code>/<ini_j>/<tdelta>")
def ts_ame_snow(code,ini_j,tdelta):
  get_snow(code,ini_j,tdelta)
  return render_template("ts_ame_snow.html",title="snow ts grapgh")
  # return f"<h1>snow test{code}{ini_j}{tdelta}</h1>"


if __name__ == "__main__":
  com ="sshpass -p grid123 ssh -L 5000:localhost:5000 griduser@133.105.83.72"
  subprocess.run(com,shell=True)
  print("end port forwarding...5000")
  app.run(host='0.0.0.0', port=5000, debug=True)
