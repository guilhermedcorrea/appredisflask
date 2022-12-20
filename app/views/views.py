from flask import Blueprint, render_template, make_response, redirect
from celery import Celery
from app import celery

view_bp = Blueprint("index", __name__)


@view_bp.route("/")
def home():
    return render_template("dashboard.html")


