from flask import Flask
#import do banco de dados
from conf.database import init_db

# módulos 
from control.index import index_bp

app = Flask(__name__)


#Conexao Geral do meu app
init_db(app)

#Registro de controladores
app.register_blueprint(index_bp)

if __name__ == "__main__":
    app.run(debug=True)
