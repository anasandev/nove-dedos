from conexao import get_connection


def cadastrar_empresa(emp_nome, emp_cnpj, emp_email, emp_tel, emp_cep, emp_rua, 
                      emp_numero, emp_complemento, emp_bairro, emp_cidade, emp_estado, emp_pais, emp_data_criacao):
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    INSERT INTO tb_empresa (
        emp_nome,
        emp_cnpj,
        emp_email,
        emp_tel,
        emp_cep,
        emp_rua,
        emp_numero,
        emp_complemento,
        emp_bairro,
        emp_cidade,
        emp_estado,
        emp_pais,
        emp_data_criacao
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    dados = (
        emp_nome,
        emp_cnpj,
        emp_email,
        emp_tel,
        emp_cep,
        emp_rua,
        emp_numero,
        emp_complemento,
        emp_bairro,
        emp_cidade,
        emp_estado,
        emp_pais,
        emp_data_criacao,
    )

    cursor.execute(comando, dados)
    conexao.commit()
    cursor.close()
    conexao.close()


def listar_empresas():
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = 'SELECT emp_id, emp_nome, emp_cnpj, emp_email, emp_tel, emp_cidade FROM tb_empresa'
    cursor.execute(comando)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados


def obter_empresa_por_id(emp_id):
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = 'SELECT * FROM tb_empresa WHERE emp_id = %s'
    cursor.execute(comando, (emp_id,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado


def atualizar_empresa(emp_id, emp_nome, emp_cnpj, emp_email, emp_tel, emp_cep, emp_rua, 
                      emp_numero, emp_complemento, emp_bairro, emp_cidade, emp_estado, emp_pais):
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    UPDATE tb_empresa
    SET
        emp_nome = %s,
        emp_cnpj = %s,
        emp_email = %s,
        emp_tel = %s,
        emp_cep = %s,
        emp_rua = %s,
        emp_numero = %s,
        emp_complemento = %s,
        emp_bairro = %s,
        emp_cidade = %s,
        emp_estado = %s,
        emp_pais = %s
    WHERE emp_id = %s
    '''

    dados = (
        emp_nome,
        emp_cnpj,
        emp_email,
        emp_tel,
        emp_cep,
        emp_rua,
        emp_numero,
        emp_complemento,
        emp_bairro,
        emp_cidade,
        emp_estado,
        emp_pais,
        emp_id,
    )

    cursor.execute(comando, dados)
    conexao.commit()
    cursor.close()
    conexao.close()


def deletar_empresa(emp_id):
    conexao = get_connection()
    cursor = conexao.cursor()

    # Verificar se existe algum produto vinculado
    verificar = 'SELECT COUNT(*) FROM tb_produto WHERE pro_emp_id = %s'
    cursor.execute(verificar, (emp_id,))
    quantidade = cursor.fetchone()[0]

    if quantidade > 0:
        cursor.close()
        conexao.close()
        return False, f"Não é possível deletar a empresa. Existem {quantidade} produto(s) vinculado(s)."

    comando = 'DELETE FROM tb_empresa WHERE emp_id = %s'
    cursor.execute(comando, (emp_id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return True, "Empresa deletada com sucesso!"
