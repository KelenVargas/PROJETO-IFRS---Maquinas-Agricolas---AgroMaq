from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy #importar certinho
import os

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
    
@index_bp.route("/auth/loginAdmin", methods=["POST"]) #pronto e testado
def loginAdmin(): 
    username = request.form.get("username")
    password = request.form.get("password") #validação fixa para um admin
    
    if username == os.getenv("ADMIN_USER") and password == os.getenv("ADMIN_PASS"):
        return jsonify({
            "success": True, 
            "message": "Login realizado com sucesso! Bem-vindo ao sistema AgroMaq."})
    else:
        return jsonify({ 
            "success": False, 
            "message": "Usuário ou senha inválidos. Tente novamente." })
                
   


@index_bp.route("/auth/login", methods=["POST"])
def login(): 
   
    username = request.form.get("username")
    password = request.form.get("password")
   
    sql = text("SELECT id, usuario, email FROM usuarios WHERE usuario = :u AND senha = :p")
    
    try:
       
        result = db.session.execute(sql, {"u": username, "p": password}).fetchone()

     
        if result:
            return jsonify({
                "success": True, 
                "message": f"Bem-vindo, {username}! Login realizado com sucesso.",
                "user_id": result[0] 
            })
        else:
         
            return jsonify({ 
                "success": False, 
                "message": "Usuário ou senha inválidos no banco de dados." 
            }), 401 

    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": f"Erro de conexão: {str(e)}"}), 500
        
    
