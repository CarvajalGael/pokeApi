from flask  import Flask, render_template, request, url_for, flash
import requests

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("/index.html")