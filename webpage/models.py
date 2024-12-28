from webpage import db
from datetime import datetime

class Contatos(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)  
    data_de_criacao = db.Column(db.DateTime, default=datetime.utcnow) 
    nome = db.Column(db.String, nullable=True)  
    email = db.Column(db.String, nullable=True)  
    mensagem = db.Column(db.String, nullable=True)  
    respondido = db.Column(db.Integer, default=0)  


# Certifique-se de importar as views e models corretamente
from webpage.views import contato_old
