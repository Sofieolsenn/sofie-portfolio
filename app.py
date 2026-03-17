from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import x
import time
import uuid
import os
import requests
import json
import csv
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from icecream import ic

ic.configureOutput(prefix=f'----- | ', includeContext=True)

app = Flask(__name__)

# Set the maximum file size to 10 MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024   # 1 MB

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

##############################
##############################
##############################
def _____USER_____(): pass 
##############################
##############################
##############################

##############################
@app.context_processor
def global_variables():
    return dict (
        x = x
    )

############################## 
@app.get("/")
@app.route("/<lan>", methods=["GET", "POST"])
def view_index(lan = "english"):     
    if lan not in x.allowed_languages: lan = "english"
    x.default_language = lan
    return render_template("index.html", lan=lan)


############################# 
@app.route("/home", methods=["GET"])
def home():
    try:
        html = render_template("_home.html")
        return f"""<browser mix-update="#SPA-container">{ html }</browser>"""
    except Exception as ex:
        ic(ex)
        return "error"


############################# 
@app.route("/about", methods=["GET"])
def about():
    try:
        html = render_template("_about.html")
        return f"""<browser mix-update="#SPA-container">{ html }</browser>"""
    except Exception as ex:
        ic(ex)
        return "error"


############################# 
@app.route("/projects", methods=["GET"])
def projects():
    try:
        html = render_template("_projects.html")
        return f"""<browser mix-update="#SPA-container">{ html }</browser>"""
    except Exception as ex:
        ic(ex)
        return "error"


############################# 
@app.route("/abilities", methods=["GET"])
def abilities():
    try:
        html = render_template("_abilities.html")
        return f"""<browser mix-update="#SPA-container">{ html }</browser>"""
    except Exception as ex:
        ic(ex)
        return "error"


############################# 
@app.route("/services", methods=["GET"])
def services():
    try:
        html = render_template("_services.html")
        return f"""<browser mix-update="#SPA-container">{ html }</browser>"""
    except Exception as ex:
        ic(ex)
        return "error"


############################# 
@app.route("/contact", methods=["GET"])
def contact():
    try:
        html = render_template("_contact.html")
        return f"""<browser mix-update="#SPA-container">{ html }</browser>"""
    except Exception as ex:
        ic(ex)
        return "error"


##############################
@app.get("/get-data-from-sheet")
def get_data_from_sheet():
    try:
        url= f"https://docs.google.com/spreadsheets/d/{x.google_spread_sheet_key}/export?format=csv&id={x.google_spread_sheet_key}"
        res=requests.get(url=url)
        csv_text = res.content.decode('utf-8')
        csv_file = io.StringIO(csv_text)
       
        data = {}
        reader = csv.DictReader(csv_file)
        for row in reader:
            item = {
                'english': row['english'],
                'danish': row['danish'],
                'japanese': row['japanese'],
            }
            data[row['key']] = item

        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        with open("dictionary.json", 'w', encoding='utf-8') as f:
            f.write(json_data)
 
        return "ok"
    except Exception as ex:
        ic(ex)
        return str(ex)

