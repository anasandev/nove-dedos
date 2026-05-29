import mysql.connector
# Define a função para obter uma conexão com o banco de dados MySQL
# Não esquecer de passar os parametros do mysql da sua maquina 
def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="admin",
        database="db_9dedos"
    )
