
from app import db
from sqlalchemy import text


def call_procedure_pedidos(ref, id):
    try:
        with db.engine.begin() as conn:
            exec = (text(
                    """EXEC Pedidos.SP_getpedidos @CodigoPedido = {}, @IdUnidade = {}""".format(ref, id)))
                        
            exec_produtos = conn.execute(exec)

            return exec_produtos
    except:
            print('erro')

