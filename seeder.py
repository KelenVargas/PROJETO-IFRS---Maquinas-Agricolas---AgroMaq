from conf.database import db, init_db
from flask import Flask
import random

app = Flask(__name__)
init_db(app)

class Produtos(db.Model):
    __tablename__ = 'produtos'
    id_produto = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text)
    preco_unitario = db.Column(db.Numeric(12,2), nullable=False)
    disponibilidade_estoque = db.Column(db.Integer, default=0)

with app.app_context():
    categorias = ["Peças", "Insumos", "Sementes", "Equipamentos", "Defensivos", "Máquinas"]
    
    nomes_base = [
        "Trator Agrícola", "Colheitadeira", "Pulverizador", "Adubo Orgânico",
        "Sementes de Milho", "Herbicida", "Pneu Trator", "Sistema de Irrigação",
        "Plantadeira Automática", "Adubo Nitrogenado", "Sementes de Soja",
        "Pulverizador Motorizado", "Herbicida Ultra", "Trator Compacto",
        "Colheitadeira Mini", "Sistema de Aspersão"
    ]

    descricoes_base = [
        "Equipamento robusto para grandes lavouras",
        "Ideal para aumentar produtividade",
        "Ferramenta essencial para pequenos produtores",
        "Produto de alta qualidade para agricultura moderna"
    ]

    for i in range(42):
        nome = f"{random.choice(nomes_base)} {i+9}"
        descricao = random.choice(descricoes_base)
        categoria = random.choice(categorias)
        preco = round(random.uniform(50, 5000), 2)
        estoque = random.randint(1, 500)

        produto = Produtos(
            nome_produto=nome,
            categoria=categoria,
            descricao=descricao,
            preco_unitario=preco,
            disponibilidade_estoque=estoque
        )
        db.session.add(produto)

    db.session.commit()
    print("Seeder concluído: 42 produtos adicionados com nomes e descrições reais!")
