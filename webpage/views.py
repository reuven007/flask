from webpage import app, db
from flask import render_template, request, redirect, url_for, Flask, flash
from webpage.models import Contatos   
from webpage.forms import ContatoForm, UserForm , LoginForm, PostForm
from flask_login import  login_user, logout_user, login_required, current_user
from webpage.models import User , Post
from flask_mail import Mail, Message



@app.route("/", methods=['GET', 'POST'])
def home():
    usuario = 'ReNewUser'    
    print(current_user.is_authenticated)    
    form = LoginForm()    
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
                              
    context = {
        'usuario': usuario          
    }
    return render_template("index.html", context=context, form=form)  # Passando o formulário

  


@app.route("/cadastro/", methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()  # O método `save` agora retorna o objeto User
        if user:  # Verifica se o usuário foi criado corretamente
            login_user(user, remember=True)

            # Enviar e-mail de boas-vindas
            msg = Message('Bem-vindo à Plataforma ReDeveloper', recipients=[user.email])
            msg.body = 'Olá, seja bem-vindo à plataforma ReDeveloper! Estamos felizes em tê-lo conosco.'
            try:
                mail.send(msg)
                flash('Cadastro realizado com sucesso. Um e-mail de boas-vindas foi enviado!', 'success')
            except Exception as e:
                flash(f'Ocorreu um erro ao enviar o e-mail: {str(e)}', 'error')

            return redirect(url_for('home'))
        else:
            flash('Erro ao criar o usuário. Por favor, tente novamente.', 'error')    
    return render_template('cadastro.html', form=form)
        
            

@app.route("/contato_old/", methods=['GET', 'POST'])
@login_required
def contato_old():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():  # Valida o formulário
        user = form.save_contato()  # Salva o contato
        context['mensagem'] = 'Cadastro realizado com sucesso!'  # Mensagem de sucesso
        print("Contato salvo:", user)  # Verifique se o contato foi salvo no banco
    else:
        print("Formulário inválido:", form.errors)  # Verifique se há erros na validação do formulário
    
    return render_template('contato.html', context=context, form=form)




@app.route("/contato/lista", methods=["GET", "POST"]) 
@login_required  
def contato_lista():
    
    # if current_user.nome != 'Rodrigo': return redirect ('/')
    # print(current_user.id )
        
    pesquisar = request.args.get('pesquisar', '')          
    dados = Contatos.query.order_by('nome')
    if pesquisar != '':
        dados = dados.filter_by(nome=pesquisar)        
        print(dados.all())
    context = {'dados':dados.all()}        
    return render_template('contato_lista.html', context=context)
 
 
 
@app.route('/contato/<int:id>')
@login_required
def contatoDetail(id):
    obj = Contatos.query.get(id)
    
    return render_template('contato_detail.html', obj= obj)



@app.route("/sair")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))  # Redireciona para a home após o logout


      
@app.route("/post/novo/", methods=["GET", "POST"])
@login_required
def PostNovo():
    form = PostForm()
    if form.validate_on_submit():  # Valida o formulário
        form.save(current_user.id)
        return redirect(url_for('home'))
    return render_template('post_novo.html', form=form)

   
   
@app.route("/post/lista/", methods=["GET", "POST"])
@login_required

def PostLista():    
    print(type(Post))  # Deve retornar algo como <class 'flask_sqlalchemy.model.DefaultMeta'>
    posts = Post.query.all()
    return render_template('post_lista.html', posts=posts)  

  
@app.route('/post_detail/<int:id>')
@login_required
def Post_detail(id):    
    post = Post.query.get(id)
    form = PostForm()
    if form.validate_on_submit():  # Valida o formulário
        form.save(current_user.id)
        return redirect(url_for('Post_detail'))
    return render_template('post.html', post=post, form=form)     

        

@app.route('/deletar/<int:id>', methods=['POST'])
@login_required
def deletar_contato(id):
    # Busca o contato pelo ID ou retorna 404 se não encontrado
    contato = Contatos.query.get_or_404(id)    
    # Deleta o contato do banco de dados
    db.session.delete(contato)
    db.session.commit()    
    # Redireciona para a lista de contatos
    return redirect(url_for('contato_lista'))



# # Formato nao recomendado
login_required
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


