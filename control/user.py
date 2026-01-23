
from flask import Blueprint, request, jsonify 
from sqlalchemy import text 
from conf.database import db
user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route("/cadastro", methods=["POST"])
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

    
    