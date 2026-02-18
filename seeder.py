from flask import Flask
import random
from conf.database import db, init_db
from models import Produtos

app = Flask(__name__)
init_db(app)



    
with app.app_context():
    
    
    nomes_base = [
        "Trator Agrícola", "Colheitadeira", "Pulverizador", "Adubo Orgânico",
        "Sementes de Milho", "Herbicida", "Pneu Trator", "Sistema de Irrigação",
        "Plantadeira Automática", "Adubo Nitrogenado", "Sementes de Soja",
        "Pulverizador Motorizado", "Herbicida Ultra", "Trator Compacto",
        "Colheitadeira Mini", "Sistema de Aspersão"
    ]

    print("Iniciando o seeder organizado...")

    for i in range(42):
        # Escolhemos o nome primeiro
        nome_escolhido = random.choice(nomes_base)
        nome_final = f"{nome_escolhido} {i+9}" # Mantendo seu padrão de numeração

        # 2. Lógica simples: O nome define a categoria e a descrição
        if "Trator" in nome_escolhido or "Colheitadeira" in nome_escolhido or "Plantadeira" in nome_escolhido:
            categoria = "Máquinas"
            descricao = "Equipamento robusto para grandes lavouras"
            preco = round(random.uniform(50000, 200000), 2) # Preço de máquina

        elif "Adubo" in nome_escolhido or "Herbicida" in nome_escolhido:
            categoria = "Insumos"
            descricao = "Produto de alta qualidade para agricultura moderna"
            preco = round(random.uniform(50, 500), 2)

        elif "Sementes" in nome_escolhido:
            categoria = "Sementes"
            descricao = "Ideal para aumentar produtividade"
            preco = round(random.uniform(100, 800), 2)

        elif "Sistema" in nome_escolhido or "Pulverizador" in nome_escolhido:
            categoria = "Equipamentos"
            descricao = "Ferramenta essencial para produtores"
            preco = round(random.uniform(1000, 15000), 2)

        else:
            categoria = "Peças"
            descricao = "Peça de reposição original"
            preco = round(random.uniform(20, 1000), 2)

        estoque = random.randint(1, 500)

        # 3. Criamos o objeto com os dados vinculados corretamente
        produto = Produtos(
            nome_produto=nome_final,
            categoria=categoria,
            descricao=descricao,
            preco_unitario=preco,
            disponibilidade_estoque=estoque
        )
        db.session.add(produto)

    db.session.commit()
    print("✅ Seeder concluído: 42 produtos adicionados de forma organizada!")
    
    
    