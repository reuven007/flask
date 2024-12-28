from webpage import app, db
from flask import render_template, request, redirect, url_for
from webpage.models import Contatos   
from webpage.forms import ContatoForm  

@app.route("/")
def home():
    context = {}
    return render_template('index.html', context=context)



@app.route("/contato_old/", methods=['GET', 'POST'])
def contato_old():
    form = ContatoForm()
    context = {}
    if  form.validate_on_submit():
        form.save()
        
        context['mensagem'] = 'Cadastro realizado com sucesso!'
        print("Mensagem de sucesso: ", context['mensagem'])  # Verifique se a mensagem aparece no console
       
    return render_template('contato.html', context=context, form=form)



@app.route("/contato/lista")    
def contato_lista():
    pesquisar = request.args.get('pesquisar', '')   
        
    dados = Contatos.query.order_by('nome')

    if pesquisar != '':
        dados = dados.filter_by(nome=pesquisar)        
        print(dados.all())
        
    context = {'dados':dados.all()}
        
    return render_template('contato_lista.html', context=context)
 
 
 
@app.route('/contato/<int:id>')
def contatoDetail(id):
    obj = Contatos.query.get(id)
    
    return render_template('contato_detail.html', obj= obj)



# # Formato nao recomendado
# @app.route("/contato_old/", methods=['GET', 'POST'])
# def contato_old():
#     context = {}
    
    
#     if request.method == 'GET':
#         pesquisar = request.args.get('pesquisar')
#         print('GET', pesquisar)
#         context.update({'pesquisar', pesquisar})
        
#     if request.method == 'POST':            
#             nome=request.form['nome'],
#             email=request.form['email'],
#             mensagem=request.form['mensagem'],
                    
#             contato = Contatos(
#                 nome = nome, 
#                 email = email, 
#                 mensagem = mensagem
#             )            
            
#             db.session.add(contato)
#             db.session.commit()
#             context['mensagem'] = 'Contato enviado com sucesso!'
       
#     return render_template('contato_old.html', context=context)


