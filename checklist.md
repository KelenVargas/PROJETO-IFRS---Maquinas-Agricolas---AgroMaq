*Mês 1: Fundação e Autenticação*
• Foco: Configuração de ambiente, conexão com Banco e Segurança.
• Entregáveis (Git):
• [x] Repositório criado com .gitignore (python) e requirements.txt.
• [x] Conexão com PostgreSQL configurada
        • [ ] Opcional pesquisar o uso de variáveis de ambiente .env (vamos precisar
        no RENDER).
• [x] Modelagem dos dados em JSON para entender o problema (objetos)
• [x] Modelagem de Dados (SQLAlchemy ou SQL Puro): Criação das tabelas User
e Lead (baseado na estrutura do doc original: id, nome, status, score) .
• [x] Rota POST /auth/login: Sistema de login retornando True ou False
• [ ] Opcional pesquisar e implementar (JWT).
• [ ] Rota POST /auth/register: Criação de novos usuários (vendedores).
----------------------------------------------------------------------------------------------------------

*Mês 2: Core Business (CRUD de Leads e "ERP")*
• Foco: Regras de negócio e manipulação de dados principais.
• Entregáveis (Git):
• [ ] CRUD de Leads: Rotas GET, POST, PUT, DELETE para /leads.
• [ ] Simulação ERP: Criar tabela Produto
• [ ] Criar dados ficticions uma boa ideia de pesquisa é um script Python (seeder) que
popula o banco com 50 produtos fictícios para rodar sem a necessidade do flask ou
em uma rota de testes.
• [ ] Lógica de Score: Ao criar um Lead, se ele tiver email E telefone, score =
100, senão score = 50.
• [ ] Validação: Impedir cadastro de Lead sem nome.
• [ ] Criar todos os Cruds e ir salvando as collections no Postman (adicionar o
professor como colaborador).
----------------------------------------------------------------------------------------------------------

*Mês 3: Métricas, Documentação e Deploy*
• Foco: Inteligência de dados e publicação.
• Entregáveis (Git):
• [ ] Rota GET /dashboard/metrics: Retornar JSON com contagem de leads por
status e valor total de vendas simuladas.
• [ ] Collection do Postman: Arquivo .json exportado com todas as rotas testadas e
funcionando.
• [ ] Deploy no Render: API acessível publicamente (ex: https://meu-crmapi.onrender.com).
• [ ] README.md: Instruções de como rodar localmente e link da documentação.
