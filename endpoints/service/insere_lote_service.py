import logging
import requests
from datetime import datetime

from models.model import LoteModel, CartaoModel
from config.logger import log
from utils.responses.messages import (
    MSG_FILE_NOT_FOUND,
    MSG_DECODE_ERROR,
    MSG_INDEX_ERROR,
    MSG_BAD_FORMAT,
    MSG_ATRIBUTE_ERROR,
    MSG_KEY_ERROR,
    MSG_LOTE_INSERT_ERRO,
)
class InsereLoteService:

    def __init__(self):
        self.lote_tratado = None

    def insere_lote_request(self, file, login_request):
        """
        service responsavel por inserer um lote de cartoes
        """
        log(f"user {login_request.get("user_name")} : iniciando requisição de inserer lote de cartoes")
        try:
            lista_cartao, objeto_lote = self.parse_txt(file)
            retorno, erros = objeto_lote.save_lote_to_db(lista_cartao)
            log(f"user {login_request.get("user_name")} : inserção de cartao realizada com sucesso")

            return retorno, erros

        except requests.exceptions.RequestException as e:
            log(f"user {login_request.get("user_name")} : erro ao insere o lote de cartoes")

            return None, str(e)
        
    def parse_txt(self, file):
        try:
            self.lote_tratado = [linha for linha in file.getlist('')[0].read().decode('utf-8').split("\n") if linha.strip()]
            nome_cartao = self.get_nome()
            lote_data = self.get_lote_data()
            lista_cartao = []
            objeto_lote = LoteModel(self.get_qtd_registro(), lote_data, self.get_nr_lote())
            for registro in range(1, len(self.lote_tratado)-1):
                lista_cartao.append(CartaoModel(self.get_nr_cartao(registro), nome_cartao, lote_data))
            
            return lista_cartao, objeto_lote
        except FileNotFoundError as e:
            return MSG_FILE_NOT_FOUND
        except UnicodeDecodeError as e:
            return MSG_DECODE_ERROR
        except IndexError as e:
            return MSG_INDEX_ERROR
        except ValueError as e:
            return MSG_BAD_FORMAT
        except AttributeError as e:
            return MSG_ATRIBUTE_ERROR
        except KeyError as e:
            return MSG_KEY_ERROR
        except Exception as e:
            return MSG_LOTE_INSERT_ERRO
        
    def get_nome(self):
        return self.lote_tratado[0][:28].strip()
    
    def get_lote_data(self):
        return datetime.strptime(self.lote_tratado[0][29:37], "%Y%m%d")
    
    def get_nr_lote(self):
        return self.lote_tratado[0][41:45]
    
    def get_qtd_registro(self):
        return int(self.lote_tratado[0][45:51])
    
    def get_nr_cartao(self, registro):
        return self.lote_tratado[registro][8:26]
