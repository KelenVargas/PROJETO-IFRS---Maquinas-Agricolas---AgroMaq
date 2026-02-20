from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()# Carrega as variáveis do .env

db = SQLAlchemy()

def init_db(app):
    # Puxa a URL completa do banco do arquivo .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    db.init_app(app)
