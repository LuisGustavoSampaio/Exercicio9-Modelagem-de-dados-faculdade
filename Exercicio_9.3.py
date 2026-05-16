import sqlite3
import re

def email_valido(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def busca_usuario_por_email(email_digitado):
    if not email_valido(email_digitado):
        return "E-mail inválido"

    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    query = "SELECT nome, email FROM usuarios WHERE email = ?"

    cursor.execute(query, (email_digitado,))

    resultado = cursor.fetchone()

    conexao.close()

    return resultado
