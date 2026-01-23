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
                
   


   
        
    
