from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy #importar certinho

from conf.database import db

index_bp = Blueprint('index', __name__, url_prefix = '/index') 


@index_bp.route("/", methods=["GET"]) #pronto e testado - funcionando com o banco de dados
def index():    
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"mensagem": "Sistema AgroMaq funcionando!"})
    except Exception :
        return jsonify({"erro": "Banco de dados não está funcionando"})
    
    
# Rota de login admin
    
@index_bp.route("/auth/login", methods=["POST"]) #pronto e testado
def login(): 
    username = request.form.get("username")
    password = request.form.get("password") #validação fixa para um admin
    if username == "admin" and password == "1234":
        return jsonify({
            "success": True, 
            "message": "Login realizado com sucesso! Bem-vindo ao sistema AgroMaq."})
    else:
        return jsonify({ 
            "success": False, 
            "message": "Usuário ou senha inválidos. Tente novamente." })
                
   
@index_bp.route("/cadastro", methods=["POST"])
def novoUsuario():
    # Dados do formulário
    usuarioNovo = request.form.get("usuario")
    senha = request.form.get("senha")
    email = request.form.get("email")

    # Verificação de campos obrigatórios
    if not usuarioNovo or not senha or not email:
        return jsonify({
            "success": False,
            "message": "Todos os campos (usuario, senha, email) são obrigatórios."
        }), 400

    # Verifica se já existe usuário com o mesmo nome 
    verifica_usuario_sql = text("SELECT id FROM usuarios WHERE usuario = :usuario") 
    verifica_usuario = db.session.execute(verifica_usuario_sql, {"usuario": usuarioNovo}).fetchone()
    if verifica_usuario:
        return jsonify({
            "success": False,
            "message": f"O nome de usuário '{usuarioNovo}' já está em uso. Escolha outro."
            }), 400
        
    # Verifica se já existe usuário com o mesmo e-mail
    verifica_sql = text("SELECT id FROM usuarios WHERE email = :email")
    verifica = db.session.execute(verifica_sql, {"email": email}).fetchone()

    if verifica:
        return jsonify({
            "success": False,
            "message": f"O e-mail '{email}' já está cadastrado. Tente o recuperar senha ou faça login!!"
        }), 400

    # SQL de inserção
    sql = text("""
        INSERT INTO usuarios (usuario, senha, email)
        VALUES (:usuario, :senha, :email)
        RETURNING id
    """)
    dados = {"usuario": usuarioNovo, "senha": senha, "email": email}
    result = db.session.execute(sql, dados)
    db.session.commit()

    id = result.fetchone()[0]

    return jsonify({
        "success": True,
        "message": f"Usuário '{usuarioNovo}' cadastrado com sucesso!",
        "dados": {
            "id": id,
            "usuario": usuarioNovo,
            "email": email
        }
    }), 201

    
    
