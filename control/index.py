from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy #importar certinho

from conf.database import db

index_bp = Blueprint('index', __name__, url_prefix = '/index') 


@index_bp.route("/", methods=["GET"])
def index():    
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"mensagem": "Sistema AgroMaq funcionando!"})
    except Exception :
        return jsonify({"erro": "Banco de dados não está funcionando"})
    
    
# Rota de login
    
@index_bp.route("/auth/login", methods=["POST"]) 
def login(): 
    data = request.get_json() 
    username = data.get("username")
    password = data.get("password") #validação fixa
    if username == "admin" and password == "1234":
        return jsonify({
            "success": True, 
            "message": "Login realizado com sucesso! Bem-vindo ao sistema AgroMaq."})
    else:
        return jsonify({ 
            "success": False, 
            "message": "Usuário ou senha inválidos. Tente novamente." })