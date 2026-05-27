from conexao import get_connection
import pwinput


def fazer_login():
    usuario = input("Email: ")
    senha = pwinput.pwinput(prompt='Senha: ', mask='*') #pwipwi :3

    conexao = get_connection()
    cursor = conexao.cursor()

    sql = "SELECT * FROM tb_usuario WHERE usu_email = %s AND usu_senha = %s"
    valores = (usuario, senha)

    cursor.execute(sql, valores)
    resultado = cursor.fetchone()

    cursor.close( )
    conexao.close()

    if resultado:
        print("Login realizado!")
        return True

    print("Usuário ou senha incorretos!")
    return False