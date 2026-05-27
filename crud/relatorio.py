from conexao import get_connection
from datetime import datetime


def relatorio_empresas():
    """Gera relatório de todas as empresas cadastradas com quantidade de produtos."""
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    SELECT 
        e.emp_id,
        e.emp_nome,
        e.emp_cnpj,
        e.emp_email,
        e.emp_cidade,
        COUNT(p.pro_id) as total_produtos,
        SUM(est.est_quantidade) as quantidade_total_estoque,
        COALESCE(SUM(p.pro_preco * est.est_quantidade), 0) as valor_estoque
        FROM tb_empresa e
        LEFT JOIN tb_produto p ON e.emp_id = p.pro_emp_id
        LEFT JOIN tb_estoque est ON p.pro_id = est.est_pro_id
        GROUP BY e.emp_id, e.emp_nome, e.emp_cnpj, e.emp_email, e.emp_cidade
        ORDER BY e.emp_nome
    '''
    
    cursor.execute(comando)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados


def relatorio_produtos_por_empresa(emp_id):
    """Gera relatório de produtos vinculados a uma empresa específica."""
    conexao = get_connection()
    cursor = conexao.cursor()

    emp_comando = 'SELECT emp_nome, emp_cnpj FROM tb_empresa WHERE emp_id = %s'
    cursor.execute(emp_comando, (emp_id,))
    empresa_info = cursor.fetchone()

    if not empresa_info:
        cursor.close()
        conexao.close()
        return None, []

    prod_comando = '''
    SELECT 
        p.pro_id,
        p.pro_nome,
        p.pro_marca,
        p.pro_descricao,
        p.pro_preco,
        p.pro_data_validade,
        COALESCE(est.est_quantidade, 0) as quantidade_estoque,
        COALESCE(p.pro_preco * est.est_quantidade, 0) as valor_total
        FROM tb_produto p
        LEFT JOIN tb_estoque est ON p.pro_id = est.est_pro_id
        WHERE p.pro_emp_id = %s
        ORDER BY p.pro_nome
        '''
    
    cursor.execute(prod_comando, (emp_id,))
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return empresa_info, produtos


def relatorio_estoque_geral():
    """Gera relatório de estoque geral de todos os produtos."""
    conexao = get_connection()
    cursor = conexao.cursor()

    comando = '''
    SELECT 
        e.emp_nome,
        p.pro_nome,
        p.pro_marca,
        est.est_quantidade,
        p.pro_preco,
        (est.est_quantidade * p.pro_preco) as valor_total,
        p.pro_data_validade
        FROM tb_produto p
        JOIN tb_empresa e ON p.pro_emp_id = e.emp_id
        LEFT JOIN tb_estoque est ON p.pro_id = est.est_pro_id
        ORDER BY e.emp_nome, p.pro_nome
        '''
    
    cursor.execute(comando)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados


def gerar_relatorio_empresas_em_arquivo(nome_arquivo='relatorio_empresas.txt'):
    """Gera relatório de empresas e salva em arquivo."""
    resultados = relatorio_empresas()
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("=" * 100 + "\n")
        f.write("RELATÓRIO DE EMPRESAS\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 100 + "\n\n")

        for empresa in resultados:
            f.write(f"ID: {empresa[0]}\n")
            f.write(f"Nome: {empresa[1]}\n")
            f.write(f"CNPJ: {empresa[2]}\n")
            f.write(f"Email: {empresa[3]}\n")
            f.write(f"Cidade: {empresa[4]}\n")
            f.write(f"Total de Produtos: {empresa[5]}\n")
            f.write(f"Quantidade em Estoque: {empresa[6] or 0}\n")
            f.write(f"Valor Total do Estoque: R$ {empresa[7]:.2f}\n")
            f.write("-" * 100 + "\n\n")

    return nome_arquivo


def gerar_relatorio_produtos_empresa_em_arquivo(emp_id, nome_arquivo='relatorio_produtos.txt'):
    """Gera relatório de produtos de uma empresa e salva em arquivo."""
    empresa_info, produtos = relatorio_produtos_por_empresa(emp_id)

    if not empresa_info:
        return False, "Empresa não encontrada."

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("=" * 100 + "\n")
        f.write("RELATÓRIO DE PRODUTOS POR EMPRESA\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 100 + "\n\n")
        
        f.write(f"Empresa: {empresa_info[0]}\n")
        f.write(f"CNPJ: {empresa_info[1]}\n")
        f.write("-" * 100 + "\n\n")

        if not produtos:
            f.write("Nenhum produto cadastrado para esta empresa.\n")
        else:
            for produto in produtos:
                f.write(f"ID: {produto[0]}\n")
                f.write(f"Nome: {produto[1]}\n")
                f.write(f"Marca: {produto[2]}\n")
                f.write(f"Descrição: {produto[3]}\n")
                f.write(f"Preço: R$ {produto[4]:.2f}\n")
                f.write(f"Data de Validade: {produto[5]}\n")
                f.write(f"Quantidade em Estoque: {produto[6]}\n")
                f.write(f"Valor Total em Estoque: R$ {produto[7]:.2f}\n")
                f.write("-" * 100 + "\n\n")

    return True, f"Relatório salvo em: {nome_arquivo}"


def gerar_relatorio_estoque_em_arquivo(nome_arquivo='relatorio_estoque.txt'):
    """Gera relatório de estoque geral e salva em arquivo."""
    resultados = relatorio_estoque_geral()

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("=" * 100 + "\n")
        f.write("RELATÓRIO DE ESTOQUE GERAL\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 100 + "\n\n")

        f.write(f"{'Empresa':<30} | {'Produto':<25} | {'Marca':<15} | {'Qtd':<5} | {'Preço':<12} | {'Total':<15} | {'Validade':<12}\n")
        f.write("-" * 100 + "\n")

        valor_total_geral = 0
        for linha in resultados:
            emp_nome = str(linha[0])[:30]
            pro_nome = str(linha[1])[:25]
            marca = str(linha[2])[:15]
            qtd = linha[3] or 0
            preco = linha[4]
            valor = linha[5] or 0
            validade = str(linha[6])

            valor_total_geral += valor
            f.write(f"{emp_nome:<30} | {pro_nome:<25} | {marca:<15} | {qtd:<5} | R$ {preco:<10.2f} | R$ {valor:<13.2f} | {validade:<12}\n")

        f.write("-" * 100 + "\n")
        f.write(f"VALOR TOTAL DO ESTOQUE: R$ {valor_total_geral:.2f}\n")

    return nome_arquivo
