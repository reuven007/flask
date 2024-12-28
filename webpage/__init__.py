from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv('.env')

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '60563cee7d6cc9a67107d9f886baab5a0d58a884acc4b26e'

# Inicializa o SQLAlchemy e Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)  

# Importa as views e models
# from webpage.views import reuven_page
from webpage.models import Contatos
