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
    
class Proposta(db.Model):
    __tablename__ = 'propostas'
    id_proposta = db.Column(db.Integer, primary_key=True)
    id_produtor = db.Column(db.Integer, db.ForeignKey('produtor.id_produtor'), nullable=False)  
    data_proposta = db.Column(db.Date)
    status = db.Column(db.String(50), default='aberta')
    itens = db.relationship('ItensProposta', backref='proposta', lazy=True)
    
class Produtor(db.Model):
    __tablename__ = 'produtor'
    id_produtor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True)
    cnpj = db.Column(db.String(14), unique=True)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    tipo_cultura = db.Column(db.String(50))
    tamanho_area = db.Column(db.Numeric(10,2))
    endereco = db.Column(db.String(200))
    score = db.Column(db.Integer, default=50) 

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)