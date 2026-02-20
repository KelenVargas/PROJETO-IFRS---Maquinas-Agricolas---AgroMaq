from flask import Flask
import random
from conf.database import db, init_db
from models import Produtos, Produtor, Usuarios  
from sqlalchemy import text

app = Flask(__name__)
init_db(app)

def run_seeder():
    with app.app_context():
        print("--- Iniciando Seeder AgroMaq ---")

       
        if not db.session.execute(text("SELECT 1 FROM usuarios")).fetchone():
            admin = Usuarios(usuario="admin", senha="123", email="admin@agromaq.com")
            vendedor = Usuarios(usuario="kelen", senha="123", email="kelen@agromaq.com")
            db.session.add_all([admin, vendedor])
            print("✅ Usuários de teste criados.")

        
        if not db.session.execute(text("SELECT 1 FROM produtor")).fetchone():
            l1 = Produtor(nome="Fazenda Horizonte", email="contato@horizonte.com", telefone="54999887766", score=100, tipo_cultura="Soja")
            l2 = Produtor(nome="Sítio do Vale", email=None, telefone="5433221100", score=50, tipo_cultura="Milho")
            db.session.add_all([l1, l2])
            print("✅ Leads (quente e frio) criados.")

      
        nomes_base = [
            "Trator Agrícola", "Colheitadeira", "Pulverizador", "Adubo Orgânico",
            "Sementes de Milho", "Herbicida", "Pneu Trator", "Sistema de Irrigação"
        ]

        for i in range(42):
            nome_escolhido = random.choice(nomes_base)
            nome_final = f"{nome_escolhido} Mod. {i+9}"
            
            
            if "Trator" in nome_escolhido or "Colheitadeira" in nome_escolhido:
                cat, preco = "Máquinas", round(random.uniform(80000, 300000), 2)
            elif "Sementes" in nome_escolhido or "Adubo" in nome_escolhido:
                cat, preco = "Insumos", round(random.uniform(100, 1000), 2)
            else:
                cat, preco = "Equipamentos", round(random.uniform(1500, 20000), 2)

            produto = Produtos(
                nome_produto=nome_final,
                categoria=cat,
                descricao=f"Descrição técnica do {nome_final}",
                preco_unitario=preco,
                disponibilidade_estoque=random.randint(5, 100)
            )
            db.session.add(produto)

        try:
            db.session.commit()
            print(f"✅ Seeder concluído: 42 produtos e dados de teste inseridos!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erro no Seeder: {e}")

if __name__ == "__main__":
    run_seeder()