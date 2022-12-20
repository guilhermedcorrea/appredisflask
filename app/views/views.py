from flask import Blueprint, render_template, make_response, redirect
from celery import Celery
from app import celery

view_bp = Blueprint("index", __name__)



@view_bp.route("/")
def index():
    return redirect('/admin')


@view_bp.route("/pedidos")
def pedidos():
    return render_template("dashboard.html")


@view_bp.route("/marcas")
def marcas():
    return render_template("marcas.html")




