# $Env:path += ';C:\Progra~1\PostgreSQL\14\bin'
import psycopg
print(psycopg)


class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
# metodo: verifica usuario na base no Postgre


def existe(usuario):
    # Conecta BD
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_pessoal_db_login",
        user="postgres",
        password="123456"
    ) as conexão:
        # obter cursor
        with conexão.cursor() as cursor:
            # executa comando
            cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                           (f'{usuario.login}', f'{usuario.senha}'))
            # obter resultado
            result = cursor.fetchone()
            return result != None

# def teste():
# print(existe(Usuario('admin', 'admin')))
# teste()


def menu():
    texto = '0-Sair\n1-Login\n2-Logout\n'
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input('Login:')
            senha = input('Senha:')
            usuario = Usuario(login, senha)
            print('Usuario OK!' if existe(usuario) else 'Usuario NOK')
        elif op == 2:
            usuario = None
            print('Logout realizado com sucesso')
        else:
            print('digite a opção válida')
        op == int(input(texto))


menu()
