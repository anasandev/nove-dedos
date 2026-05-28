from .produto import cadastrar_produto, listar_produtos, obter_produto_por_id, atualizar_produto, deletar_produto
from .estoque import listar_estoque, adicionar_estoque, remover_estoque
from .empresa import (cadastrar_empresa, listar_empresas, obter_empresa_por_id, 
                      atualizar_empresa, deletar_empresa)
from . import relatorio
# Define o que será exportado quando alguém importar o módulo crud
__all__ = [
    "cadastrar_produto",
    "listar_produtos",
    "atualizar_produto",
    "deletar_produto",
    "listar_estoque",
    "adicionar_estoque",
    "remover_estoque",
    "cadastrar_empresa",
    "listar_empresas",
    "obter_empresa_por_id",
    "atualizar_empresa",
    "deletar_empresa",
    "relatorio",
]
