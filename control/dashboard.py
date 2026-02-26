from flask import Blueprint, jsonify
from sqlalchemy import text
from conf.database import db


dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard/metricas', methods=['GET'])
def get_metricas():
    try:
        query_leads = text("""
            SELECT 
                COUNT(*) as total_leads,
                COUNT(*) FILTER (WHERE score = 100) as leads_ouro,
                COUNT(*) FILTER (WHERE score = 50) as leads_bronze
            FROM produtor
        """)        
        
        query_vendas = text("""
            SELECT SUM(quantidade * preco_unitario) as faturamento_total 
            FROM itens_proposta
        """)
        
        resultado_leads = db.session.execute(query_leads).mappings().one()
        resultado_vendas = db.session.execute(query_vendas).mappings().one()

        
        return jsonify({
            "leads": {
                "total_cadastrados": resultado_leads['total_leads'],
                "status": {
                    "ouro_score_100": resultado_leads['leads_ouro'],
                    "bronze_score_50": resultado_leads['leads_bronze']
                }
            },
            "financeiro": {
                "vendas_totais_reais": float(resultado_vendas['faturamento_total'] or 0)
            }
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao carregar dashboard", "details": str(e)}), 500
    
    
    
@dashboard_bp.route('/dashboard/faturamento', methods=['GET'])
def get_revenue_split():
    try:
        query = text("""
            SELECT pr.tipo_cultura, SUM(i.quantidade * i.preco_unitario) as faturamento
            FROM itens_proposta i
            JOIN propostas prop ON i.id_proposta = prop.id_proposta
            JOIN produtor pr ON prop.id_produtor = pr.id_produtor
            GROUP BY pr.tipo_cultura
            ORDER BY faturamento DESC
        """)
        resultado = db.session.execute(query).mappings().all()
        
        return jsonify({
            "segmentacao_por_cultura": [
                {"categoria": row['tipo_cultura'], "valor": float(row['faturamento'])} 
                for row in resultado
            ]
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500