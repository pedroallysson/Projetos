from flask import Blueprint, render_template
from MongoDB.MongoDBConnection import MongoDBConnection
from dotenv import load_dotenv
from Flask.auth import token_required 
import os

'''
Arquivo para renderizar os templates de cada rota
'''
load_dotenv()

pages_bp = Blueprint('pages', __name__)

uri = os.getenv('MONGO_URI')
database = os.getenv('MONGO_DATABASE')

mongo_conn = MongoDBConnection(uri, database)

'''
Rota de home(/)
renderiza o template de login no navegador do usuário
acesso para todos que tem a url
'''
@pages_bp.route('/')
def home():
    return render_template('login.html')

'''
Rota para o template de relatório apenas quando o usuário estiver logado
acesso para users/admins
'''
@pages_bp.route('/relatorio')
@token_required
def relatorio_page():

    return render_template('relatorio.html')

@pages_bp.route('/usuarios')
def usuario_page():

    return render_template('usuarios.html')

'''
Rota protegida apenas para admins
'''
@pages_bp.route('/dispositivos')
def dispositivos_page():

    return render_template('dispositivos.html')


'''
Rota de mapa das enfermarias

acesso para users/admins
'''
@pages_bp.route('/mapa')
def mapa_page():

    return render_template('mapa_enfermarias.html')