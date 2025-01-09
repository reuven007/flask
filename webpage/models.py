from webpage import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# Controle de Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)    
    
# Adicionando o modelo de Usuário e Login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  
    nome = db.Column(db.String, nullable=True)  
    sobrenome = db.Column(db.String, nullable=True)  
    email = db.Column(db.String, nullable=True) 
    senha = db.Column(db.String, nullable=True) 
    posts = db.relationship('Post', backref='user', lazy=True)
    
    

class Contatos(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)  
    data_de_criacao = db.Column(db.DateTime, default=datetime.utcnow) 
    nome = db.Column(db.String, nullable=True)  
    email = db.Column(db.String, nullable=True)  
    mensagem = db.Column(db.String, nullable=True)  
    respondido = db.Column(db.Integer, default=0) 
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    data_de_envio = db.Column(db.DateTime, default=datetime.utcnow) 
    mensagem = db.Column(db.String, nullable=True)  
    imagem = db.Column(db.String, nullable=True, default='default.png')  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


    def msg_preview(self):
        return  self.msg_preview[10]
        
        
        
        



# Certifique-se de importar as views e models corretamente
from webpage.views import contato_old
