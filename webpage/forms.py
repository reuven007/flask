from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from webpage import db, bcrypt, app
from webpage.models import Contatos, User, Post
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
import os
from werkzeug.utils import secure_filename



class UserForm(FlaskForm):
    
    nome = StringField('Nome Completo', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Senha', validators=[DataRequired(),EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')
        
   # Validação do e-mail para verificar se já existe no banco
    def validate_email(self, email):
        # Verifica se o e-mail já existe
        if User.query.filter_by(email=email.data).first():
            return ValidationError("Usuário já cadastrado com esse email !")
        
        
    # Função para salvar o usuário no banco
    def save(self):
            senha = generate_password_hash(self.senha.data)
            user = User(
            nome=self.nome.data,
            sobrenome=self.sobrenome.data,
            email=self.email.data,
            senha=senha
        )
            db.session.add(user)
            db.session.commit()
            return user  

    

class ContatoForm(FlaskForm):
    
    nome = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
    

    def save_contato(self):
        
        print(f"Salvando contato: {self.nome.data}, {self.email.data}, {self.mensagem.data}")  # Para verificar
        user = Contatos(
            nome=self.nome.data,
            email=self.email.data,
            mensagem=self.mensagem.data
        )
        db.session.add(user)
        db.session.commit()
        return user 
''

class LoginForm(FlaskForm):
   
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Logar')
    
    def login(self):
        # Recuperar o usuário do email
        user = User.query.filter_by(email=self.email.data).first()
                
        # Verificar se a senha é valida
        if user:         
            if  bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                return user
            else: 
                raise Exception ("Usuário não encontrado")
        else:
            raise Exception("Senha inválida")
    


class PostForm(FlaskForm):
    
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    imagem = FileField('imagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
    
    def save(self, user_id):
        imagem = self.imagem.data
        nome_seguro = secure_filename(imagem.filename)
        post = Post(            
            mensagem=self.mensagem.data,
            user_id=user_id,        
            imagem=nome_seguro     
    )
    
     # Constrói o caminho completo para salvar o arquivo
        caminho = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),# Pasta do projeto
        app.config['UPLOADS_FILES'],# Pasta de uploads
        'post', # Subpasta para os posts
        nome_seguro # Nome do arquivo seguro
        
    )
        imagem.save(caminho)
        # Salva o post no banco de dados
        db.session.add(post)
        db.session.commit()
