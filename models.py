# models.py
from conf.database import db

class Produtos(db.Model):
    __tablename__ = 'produtos'
    id_produto = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text)
    preco_unitario = db.Column(db.Numeric(12,2), nullable=False)
    disponibilidade_estoque = db.Column(db.Integer, default=0)

class ItensProposta(db.Model):
    __tablename__ = 'itens_proposta'
    id_item = db.Column(db.Integer, primary_key=True)
    id_proposta = db.Column(db.Integer, db.ForeignKey('propostas.id_proposta', ondelete='CASCADE'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Numeric(12,2), nullable=False)