from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from webpage import db
from webpage.models import Contatos
from flask_wtf import FlaskForm

class ContatoForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):

        print(f"Salvando contato: {self.nome.data}, {self.email.data}, {self.mensagem.data}")  # Para verificar
        contato = Contatos(
            nome=self.nome.data,
            email=self.email.data,
            mensagem=self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()
