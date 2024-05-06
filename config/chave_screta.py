import secrets
import string

#ATENÇÃO - ZONA DE PERIGO, NUNCA EM HIPOTESE ALGUMA SUBIR UMA APLICAÇÃO COM CHAVE SECRETA HARDCODE - ESCONDA EM VARIAVEL DE AMBIENTE
def gerar_chave(length=32):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    chave = ''.join(secrets.choice(caracteres) for i in range(length))
    return chave


if not globals().get('CHAVE_SECRETA'):
    CHAVE_SECRETA = gerar_chave()