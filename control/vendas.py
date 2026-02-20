from flask import Blueprint, request, jsonify 
from sqlalchemy import text 
from conf.database import db
vendas_bp = Blueprint('vendas', __name__, url_prefix='/vendas')



@vendas_bp.route('/adicionar-item', methods=['POST'])
def adicionar_item():
    # Pegamos os dados do Postman (form-data)
    id_proposta = request.form.get("id_proposta")
    id_produto = request.form.get("id_produto")
    quantidade = request.form.get("quantidade")
    preco_unitario = request.form.get("preco_unitario")

    # SQL Puro para inserir o item
    sql = text("""
        INSERT INTO itens_proposta (id_proposta, id_produto, quantidade, preco_unitario)
        VALUES (:id_p, :id_prod, :qtd, :preco)
    """)
    
    try:
        db.session.execute(sql, {
            "id_p": id_proposta,
            "id_prod": id_produto,
            "qtd": quantidade,
            "preco": preco_unitario
        })
        db.session.commit()
        return jsonify({"success": True, "message": "Item adicionado à proposta com sucesso!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": f"Erro ao inserir: {str(e)}"}), 500
    
    
@vendas_bp.route('/proposta/<int:id_proposta>/total', methods=['GET'])
def total_proposta(id_proposta):
    # SQL que multiplica quantidade por preço e soma tudo
    sql = text("""
        SELECT SUM(quantidade * preco_unitario) 
        FROM itens_proposta 
        WHERE id_proposta = :id
    """)
    
    resultado = db.session.execute(sql, {"id": id_proposta}).fetchone()
    total = resultado[0] if resultado[0] else 0
    
    return jsonify({
        "id_proposta": id_proposta,
        "total_acumulado": float(total)
    })
    
@vendas_bp.route('/produtos', methods=['GET'])
def listar_produtos():

    sql = text("SELECT * FROM produtos")
    try:
        result = db.session.execute(sql)
      
        relatorio = result.mappings().all()
        json_data = [dict(row) for row in relatorio]
        return jsonify(json_data)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao listar produtos", "details": str(e)}), 500