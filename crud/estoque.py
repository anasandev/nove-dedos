from conexao import get_connection


def listar_estoque():
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    SELECT
        e.est_id,
        p.pro_id,
        p.pro_nome,
        e.est_quantidade
    FROM tb_estoque e
    JOIN tb_produto p ON e.est_pro_id = p.pro_id
    ORDER BY p.pro_nome
    '''

    cursor.execute(comando)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados


def adicionar_estoque(pro_id, quantidade):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute('SELECT est_id, est_quantidade FROM tb_estoque WHERE est_pro_id = %s', (pro_id,))
    resultado = cursor.fetchone()

    if resultado:
        est_id, est_quantidade = resultado
        nova_quantidade = est_quantidade + quantidade
        cursor.execute('UPDATE tb_estoque SET est_quantidade = %s WHERE est_id = %s', (nova_quantidade, est_id))
    else:
        cursor.execute('INSERT INTO tb_estoque (est_quantidade, est_pro_id) VALUES (%s, %s)', (quantidade, pro_id))

    conexao.commit()
    cursor.close()
    conexao.close()


def remover_estoque(pro_id, quantidade):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute('SELECT est_id, est_quantidade FROM tb_estoque WHERE est_pro_id = %s', (pro_id,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Produto sem estoque registrado.")
        cursor.close()
        conexao.close()
        return

    est_id, est_quantidade = resultado
    nova_quantidade = est_quantidade - quantidade

    if nova_quantidade < 0:
        print("Não é possível remover mais do que o estoque atual.")
        cursor.close()
        conexao.close()
        return

    cursor.execute('UPDATE tb_estoque SET est_quantidade = %s WHERE est_id = %s', (nova_quantidade, est_id))
    conexao.commit()

    cursor.close()
    conexao.close()
