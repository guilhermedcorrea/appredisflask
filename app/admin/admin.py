from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask import current_app
from flask_admin import Admin
from flask import Blueprint
import os
from dotenv import load_dotenv
from os import path
from datetime import datetime
from flask_admin.base import BaseView, expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import Admin
from sqlalchemy import text
from werkzeug.utils import secure_filename
import os
import flask_excel as excel
from datetime import datetime


load_dotenv()

uploads = os.getenv('uploads')

UPLOADFOLDER = uploads


adm = Blueprint('adm', __name__)
current_app.config["UPLOAD_FOLDER"] = os.path.join(UPLOADFOLDER,'app','uploads')
excel.init_excel(current_app)

class MyAdminIndexView(AdminIndexView):
    pass


admin = Admin(current_app, name='Admin',
              template_mode='bootstrap3', index_view=MyAdminIndexView())

current_app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True

