<h4 align="center"> 
   🌱 AgroMaq API – Gestão de Leads e Inteligência de Vendas
</h4>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=green&style=for-the-badge"/>
  <img src="https://img.shields.io/static/v1?label=DEPLOY&message=RENDER&color=blue&style=for-the-badge"/>
</p>

# 📊 API de Gestão de Leads e Inteligência de Vendas

Esta é uma API robusta desenvolvida para gerenciar o ciclo de vida de leads, simular um ERP de produtos agrícolas e fornecer métricas estratégicas para tomada de decisão.
O projeto foi construído utilizando **Python, Flask e PostgreSQL**, seguindo uma arquitetura modular e segura.

# 📌 Sobre o Projeto
O AgroMaq API é uma solução voltada para revendas de máquinas e insumos, com foco em gestão de leads B2B. A API permite desde o cadastro qualificado de produtores até a análise de faturamento por tipo de cultura, garantindo inteligência competitiva para o negócio.

## 🚀 Funcionalidades Implementadas
- **Autenticação**: Acesso restrito via login administrativo.
- **Gestão de Leads**: Cadastro com validações de CPF/CNPJ e sistema de **Score Automático** (Leads Ouro/Bronze).
- **Simulação de ERP**: Listagem de produtos (máquinas e sementes) via banco de dados.
- **Vendas Relacionais**: Sistema de Propostas e Itens de Proposta vinculados a produtores.
- **Dashboard de Inteligência**: 
    - Contagem de leads por status.
    - Valor total de vendas simuladas.
    - Análise de faturamento segmentado por tipo de cultura (Soja, Milho, etc).


## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3+
- **Framework**: Flask
- **Banco de Dados**: PostgreSQL (SQL Puro com SQLAlchemy)
- **Segurança**: Variáveis de Ambiente (`python-dotenv`)
- **Deploy**: Render

## 📋 Endpoints Principais
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/login` | Autenticação do administrador. |
| `POST` | `/leads` | Cria um novo produtor com cálculo de Score. |
| `POST` | `/vendas` | Registra uma nova venda (Proposta + Itens). |
| `GET` | `/dashboard/metricas` | Retorna (Total leads e vendas). |
| `GET` | `/dashboard/faturamento` | Retorna o lucro segmentado por cultura. |


## ⚙️ Como rodar o projeto localmente
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Configure o arquivo `.env` com suas credenciais (`DB_URL`, `ADMIN_PASS`).
5. Popule o banco (opcional): `python seeder.py`.
6. Inicie a API: `python app.py`.


> **Nota:** A Collection do Postman para testes rápidos está disponível na raiz: `AgroMaq_Collection.json`.

## 🔗 Link de Deploy
A API está disponível publicamente em: [INSIRA_SEU_LINK_DO_RENDER_AQUI]

## 👨‍💻 Autor
AgroMaq API foi desenvolvido como projeto acadêmico por:
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/KelenVargas" title="Perfil de Kelen Vargas">
        <img src="https://avatars.githubusercontent.com/u/102633488?s=400&u=bb2ccd1d002ac0cf824b55a25ff07ad6a3552d90&v=4" width="120px;" alt="Foto de Kelen Vargas"/><br>
        <sub>
          <b>Kelen Vargas</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 🏆 Créditos
👨‍🏫 Orientação:**Professor(a) Márcio Bigolin**

🏫 Instituição:**IFRS - Instituto Federal do RS/Campus Canoas & Instituto Hardware BR**
