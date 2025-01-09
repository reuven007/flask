from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


load_dotenv('.env')

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '60563cee7d6cc9a67107d9f886baab5a0d58a884acc4b26e'
app.config['UPLOADS_FILES'] = r'static/data'


# Inicializa o SQLAlchemy e Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view ='home'
bcrypt = Bcrypt(app)

# Importa as views e models
# from webpage.views import reuven_page
from webpage.models import Contatos
