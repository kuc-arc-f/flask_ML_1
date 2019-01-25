# 日本語

# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

import flaskr.views