from conexao import get_connection
from datetime import datetime


def inicializar_estoque(pro_id, quantidade, usu_id=None):
    """Cria ou atualiza o registro de estoque para um produto.
    Se `usu_id` for fornecido e `quantidade` for maior que zero, registra uma movimentação de entrada.
    """
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute('SELECT est_quantidade FROM tb_estoque WHERE est_pro_id = %s', (pro_id,))
    row = cursor.fetchone()

    if row:
        comando = 'UPDATE tb_estoque SET est_quantidade = %s WHERE est_pro_id = %s'
        cursor.execute(comando, (quantidade, pro_id))
    else:
        comando = 'INSERT INTO tb_estoque (est_quantidade, est_pro_id) VALUES (%s, %s)'
        cursor.execute(comando, (quantidade, pro_id))

    if usu_id is not None and quantidade > 0:
        comando_mov = '''
        INSERT INTO tb_movimentacao (
            mov_tipo, mov_quantidade, mov_data_movimentacao, mov_pro_id, mov_usu_id
        ) VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(comando_mov, ('entrada', quantidade, datetime.now(), pro_id, usu_id))

    conexao.commit()
    cursor.close()
    conexao.close()


def adicionar_estoque(pro_id, quantidade, usu_id=None):
    """Registra uma entrada de estoque e cria o registro se necessário."""
    if quantidade <= 0:
        raise ValueError('quantidade deve ser positiva')

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute('SELECT est_quantidade FROM tb_estoque WHERE est_pro_id = %s', (pro_id,))
    row = cursor.fetchone()

    if row:
        novo = row[0] + quantidade
        cursor.execute('UPDATE tb_estoque SET est_quantidade = %s WHERE est_pro_id = %s', (novo, pro_id))
    else:
        cursor.execute('INSERT INTO tb_estoque (est_quantidade, est_pro_id) VALUES (%s, %s)', (quantidade, pro_id))

    if usu_id is not None:
        comando_mov = '''
        INSERT INTO tb_movimentacao (
            mov_tipo, mov_quantidade, mov_data_movimentacao, mov_pro_id, mov_usu_id
        ) VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(comando_mov, ('entrada', quantidade, datetime.now(), pro_id, usu_id))

    conexao.commit()
    cursor.close()
    conexao.close()


def remover_estoque(pro_id, quantidade, usu_id=None):
    """Registra uma saída de estoque; lança ValueError se quantidade inválida ou estoque insuficiente."""
    if quantidade <= 0:
        raise ValueError('quantidade deve ser positiva')

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute('SELECT est_quantidade FROM tb_estoque WHERE est_pro_id = %s', (pro_id,))
    row = cursor.fetchone()

    if not row:
        cursor.close()
        conexao.close()
        raise ValueError('estoque inexistente para o produto')

    atual = row[0]
    if atual < quantidade:
        cursor.close()
        conexao.close()
        raise ValueError('estoque insuficiente')

    novo = atual - quantidade
    cursor.execute('UPDATE tb_estoque SET est_quantidade = %s WHERE est_pro_id = %s', (novo, pro_id))

    if usu_id is not None:
        comando_mov = '''
        INSERT INTO tb_movimentacao (
            mov_tipo, mov_quantidade, mov_data_movimentacao, mov_pro_id, mov_usu_id
        ) VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(comando_mov, ('saida', quantidade, datetime.now(), pro_id, usu_id))

    conexao.commit()
    cursor.close()
    conexao.close()


def obter_estoque_por_produto(pro_id):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute('SELECT est_quantidade FROM tb_estoque WHERE est_pro_id = %s', (pro_id,))
    row = cursor.fetchone()
    cursor.close()
    conexao.close()
    return row[0] if row else 0


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
