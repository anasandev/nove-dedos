from conexao import get_connection


def cadastrar_produto(pro_nome, pro_descricao, pro_marca, pro_preco, pro_data_validade, pro_emp_id=None):
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    INSERT INTO tb_produto (
        pro_nome,
        pro_descricao,
        pro_marca,
        pro_preco,
        pro_data_validade,
        pro_emp_id
    ) VALUES (%s, %s, %s, %s, %s, %s)
    '''

    dados = (
        pro_nome,
        pro_descricao,
        pro_marca,
        pro_preco,
        pro_data_validade,
        pro_emp_id,
    )

    cursor.execute(comando, dados)
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_produtos():
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = 'SELECT * FROM tb_produto'
    cursor.execute(comando)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados


def atualizar_produto(pro_id, pro_nome, pro_descricao, pro_marca, pro_preco, pro_data_validade, pro_emp_id=None):
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    UPDATE tb_produto
    SET
        pro_nome = %s,
        pro_descricao = %s,
        pro_marca = %s,
        pro_preco = %s,
        pro_data_validade = %s,
        pro_emp_id = %s
    WHERE pro_id = %s
    '''

    dados = (
        pro_nome,
        pro_descricao,
        pro_marca,
        pro_preco,
        pro_data_validade,
        pro_emp_id,
        pro_id,
    )

    cursor.execute(comando, dados)
    conexao.commit()

    cursor.close()
    conexao.close()


def deletar_produto(pro_id):
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = 'DELETE FROM tb_produto WHERE pro_id = %s'
    cursor.execute(comando, (pro_id,))
    conexao.commit()

    cursor.close()
    conexao.close()
