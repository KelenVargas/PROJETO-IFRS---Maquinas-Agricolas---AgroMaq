from flask import Flask
#import do banco de dados
from conf.database import init_db
from models import Produtos, ItensProposta, Proposta, Produtor, Usuarios

# módulos 
from control.index import index_bp
from control.leads import produtor_bp
from control.user import user_bp
from control.vendas import vendas_bp


app = Flask(__name__)


#Conexao Geral do meu app
init_db(app)

#Registro de controladores
app.register_blueprint(index_bp)
app.register_blueprint(produtor_bp)
app.register_blueprint(user_bp)
app.register_blueprint(vendas_bp)



if __name__ == "__main__":
    app.run(debug=True)
