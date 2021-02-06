from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
  #ロボットの出す手を決める
  return render_template("index.html")
# ルーティングの指定(ぐーのとき)
@app.route('/guu')
def guu():
  #ロボットの出す手を決める
    robot = random.randint(1,3)
    return render_template("guu.html", robot = robot)
@app.route('/choki')
def choki():
    robot = random.randint(1,3)
    return render_template("choki.html", robot = robot)
@app.route('/paa')
def paa():
    robot = random.randint(1,3)
    return render_template("paa.html", robot = robot)
app.run(host='0.0.0.0')