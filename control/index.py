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
    
    
    