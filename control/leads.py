from flask import Blueprint, request, jsonify
from sqlalchemy import text
from conf.database import db

produtor_bp = Blueprint('produtor_bp', __name__)

# GET - listar todos os produtores
@produtor_bp.route('/leads', methods=['GET'])
def get_all_produtores():
    sql_query = text("SELECT * FROM produtor")
    try:
        result = db.session.execute(sql_query)
        relatorio = result.mappings().all()
        json_data = [dict(row) for row in relatorio]
        return jsonify(json_data)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao listar produtores", "details": str(e)}), 500

# POST - criar novo produtor
@produtor_bp.route('/leads', methods=['POST'])
def create_produtor():
    data = request.form  # pega os dados do form-data
    
    # ---- Validações ----
    if not data.get("nome"):
        return jsonify({"error": "O campo 'nome' é obrigatório"}), 400
    
    if not data.get("cpf") and not data.get("cnpj"): 
        return jsonify({"error": "É obrigatório informar CPF ou CNPJ"}), 400
    
    if data.get("cpf") and len(data.get("cpf")) != 11:
        return jsonify({"error": "CPF deve ter exatamente 11 dígitos"}), 400

    if data.get("cnpj") and len(data.get("cnpj")) != 14:
        return jsonify({"error": "CNPJ deve ter exatamente 14 dígitos"}), 400
    
    # --- NOVA LÓGICA SCORE ---
    # Se tiver email E telefone = 100, senão = 50
    if data.get("email") and data.get("telefone"):
        score = 100
    else:
        score = 50
    
    sql_query = text("""
        INSERT INTO produtor (nome, cpf, cnpj, telefone, email, tipo_cultura, tamanho_area, endereco, score)
        VALUES (:nome, :cpf, :cnpj, :telefone, :email, :tipo_cultura, :tamanho_area, :endereco, :score)
    """)
    try:
        params = {
            "nome": data.get("nome"),
            "cpf": data.get("cpf"),
            "cnpj": data.get("cnpj"),
            "telefone": data.get("telefone"),
            "email": data.get("email"),
            "tipo_cultura": data.get("tipo_cultura"),
            "tamanho_area": data.get("tamanho_area"),
            "endereco": data.get("endereco"),
            "score": score
        }
        db.session.execute(sql_query, params)
        db.session.commit()
        return jsonify({"message": f"Produtor criado com sucesso! Score atribuído: {score}"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao processar os dados no banco", "details": str(e)}), 500


# PUT - atualizar produtor
@produtor_bp.route('/leads/<int:id_produtor>', methods=['PUT'])
def update_produtor(id_produtor):
    data = request.form
    if data.get("cpf") and len(data.get("cpf")) != 11:
        return jsonify({"error": "CPF deve ter exatamente 11 dígitos"}), 400

    if data.get("cnpj") and len(data.get("cnpj")) != 14:
        return jsonify({"error": "CNPJ deve ter exatamente 14 dígitos"}), 400
    
    # --- RECALCULAR SCORE NA ATUALIZAÇÃO ---
    if data.get("email") and data.get("telefone"):
        score = 100
    else:
        score = 50
    
    sql_query = text("""
        UPDATE produtor
        SET nome=:nome, cpf=:cpf, cnpj=:cnpj, telefone=:telefone, email=:email,
            tipo_cultura=:tipo_cultura, tamanho_area=:tamanho_area, endereco=:endereco,
            score=:score
        WHERE id_produtor=:id_produtor
    """)
    try:
        params = {
            "nome": data.get("nome"),
            "cpf": data.get("cpf"),
            "cnpj": data.get("cnpj"),
            "telefone": data.get("telefone"),
            "email": data.get("email"),
            "tipo_cultura": data.get("tipo_cultura"),
            "tamanho_area": data.get("tamanho_area"),
            "endereco": data.get("endereco"),
            "score": score,
            "id_produtor": id_produtor
        }

        db.session.execute(sql_query, params)
        db.session.commit()
        return jsonify({"message": f"Produtor atualizado! Novo Score: {score}"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao processar os dados no banco", "details": str(e)}), 500
        

# DELETE - remover produtor
@produtor_bp.route('/leads/<int:id_produtor>', methods=['DELETE'])
def delete_produtor(id_produtor):
    sql_query = text("DELETE FROM produtor WHERE id_produtor=:id_produtor")
    try:
        db.session.execute(sql_query, {"id_produtor": id_produtor})
        db.session.commit()
        return jsonify({"message": "Produtor removido com sucesso!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao processar os dados no banco", "details": str(e)}), 500
