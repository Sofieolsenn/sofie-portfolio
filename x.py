from flask import request, make_response, render_template
import mysql.connector
import re 
import json
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from functools import wraps

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

UPLOAD_ITEM_FOLDER = './images'

def db():
    try:
        host = "sofievooo.mysql.pythonanywhere-services.com" if "PYTHONANYWHERE_DOMAIN" in os.environ else "mariadb"
        database = "sofievooo$default" if "PYTHONANYWHERE_DOMAIN" in os.environ else "x"
        user = "sofievo" if "PYTHONANYWHERE_DOMAIN" in os.environ else "root"
        password = "MyPasswordForYou" if "PYTHONANYWHERE_DOMAIN" in os.environ else "password"

        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except mysql.connector.Error as e:
        print("DB connection error:", e, flush=True)
        raise Exception("Twitter exception - Database under maintenance", 500)


##############################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view


##############################
google_spread_sheet_key = "1gliI2Lj5nHKb6ZwiR5po29K9LEaffbalbkJVZf5SDL4"
allowed_languages = ["english", "danish", "japanese"]
default_language = "english"

##############################
def lans(key):
    with open("dictionary.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[key][default_language]

