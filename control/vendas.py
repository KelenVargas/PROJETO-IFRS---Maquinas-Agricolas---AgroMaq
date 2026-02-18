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
    # SQL que soma (quantidade * preco_unitario) de todos os itens daquela proposta
    sql = text("SELECT SUM(quantidade * preco_unitario) FROM itens_proposta WHERE id_proposta = :id")
    result = db.session.execute(sql, {"id": id_proposta}).fetchone()
    
    return jsonify({
        "id_proposta": id_proposta,
        "valor_total": float(result[0]) if result[0] else 0
    })