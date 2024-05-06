import hashlib
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship
from utils.responses.messages import MSG_DATA_ERROR_ROLLBACK

from db.data import db

class UserModel(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, nome, password):
        self.nome = nome
        self.password = self._hash_password(password)

    @classmethod
    def find_by_name(cls, nome=nome):
        return cls.query.filter_by(nome=nome).first()
    
    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True, None
        except IntegrityError as e:
            db.session.rollback()
            return False, MSG_DATA_ERROR_ROLLBACK
        except Exception as e:
            db.session.rollback()
            return False, MSG_DATA_ERROR_ROLLBACK

class LoteModel(db.Model):
    __tablename__ = 'tb_lote'

    id = db.Column(db.Integer, primary_key=True)
    qtd_registros = db.Column(db.Integer, nullable=False)
    nr_lote = db.Column(db.String, nullable=False)
    dt_inclusao = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, qtd_registros, dt_inclusao, nr_lote):
        self.qtd_registros = qtd_registros
        self.nr_lote = nr_lote
        self.dt_inclusao = dt_inclusao

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_lote_to_db(self, cartoes):
        try:
            db.session.add(self)
            db.session.commit()
            for cartao in cartoes:
                cartao.lote_id = self.id
                db.session.add(cartao)
            db.session.commit()
            return True, None
        except IntegrityError as e:
            db.session.rollback()
            return False, MSG_DATA_ERROR_ROLLBACK
        except Exception as e:
            db.session.rollback()
            return False, MSG_DATA_ERROR_ROLLBACK


class CartaoModel(db.Model):
    __tablename__ = 'tb_cartao'

    id = db.Column(db.Integer, primary_key=True)
    nr_cartao = db.Column(db.String(80), nullable=False)
    nm_cartao_nome = db.Column(db.String(80), nullable=False)
    dt_inclusao = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    lote_id = db.Column(db.Integer, ForeignKey('tb_lote.id'))

    lote = relationship('LoteModel', backref='cartoes', lazy=True)

    def __init__(self, nr_cartao, nm_cartao_nome, dt_inclusao=datetime.now(), lote_id=None):
        self.nr_cartao = nr_cartao
        self.nm_cartao_nome = nm_cartao_nome
        self.dt_inclusao = dt_inclusao
        self.lote_id = lote_id

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_numero_cartao(cls, cartao):
        return cls.query.filter_by(nr_cartao=cartao).first()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True, None
        except IntegrityError as e:
            db.session.rollback()
            return False, MSG_DATA_ERROR_ROLLBACK
        except Exception as e:
            db.session.rollback()
            return False, MSG_DATA_ERROR_ROLLBACK
