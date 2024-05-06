from flask import Flask
from flask_restful import Api

from db.data import db
from config.logger import configurar_logger
from endpoints.resource.login_resource import LoginResource
from endpoints.resource.consulta_cartao_resource import ConsultaCartaoResource
from endpoints.resource.inserir_cartao_resource import InsereCartaoResource
from endpoints.resource.inserir_lote_resource import InsereLoteResource


app = Flask(__name__)
api = Api(app)
api.prefix = '/api'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


api.add_resource(LoginResource, '/login', methods=['POST'], endpoint='/login')
api.add_resource(ConsultaCartaoResource, '/consulta-cartao/<cartao>', methods=['GET'], endpoint='/consulta_cartao_get')
api.add_resource(InsereCartaoResource, '/inserir-cartao', methods=['POST'], endpoint='/inserir_cartao_post')
api.add_resource(InsereLoteResource, '/inserir-cartao-lote', methods=['POST'], endpoint='/inserir_cartao_lote_post')



def app_start():
    db.init_app(app)
    configurar_logger()

    with app.app_context():
        db.create_all()
    return app

app = app_start()



if __name__ == '__main__':
    app.run(debug=True)