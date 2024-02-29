import json
import sys

from omie import *


exemplo = Omie("CAV").ConsultarPedido

#exemplo.nRegPorPagina = 10
#exemplo.nPagina = 2
#exemplo.nCodPed = 1620

exemplo.numero_pedido = int(sys.argv[1])

res = exemplo.executar()

try:
    codigo_pedido = res['pedido_venda_produto']['cabecalho']['codigo_pedido']
except:
    print(res)
    exit(1)

print(f"O código do pedido de número {exemplo.numero_pedido} é {codigo_pedido}")

consulta_pedido_etapa = Omie("CAV").ConsultarPedidoEtapas

consulta_pedido_etapa.nCodPed = codigo_pedido

res = consulta_pedido_etapa.executar()
try:
    print(json.dumps([x["cEtapa"]+","+x["dDtEtapa"] for x in res["etapasPedido"] if True or x["cEtapa"] in ("10", "20")], indent=2))
except:
    print(res)
