from flask import Flask, render_template
from flask_wtf import FlaskForm
from config import Config
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

from app import routes
