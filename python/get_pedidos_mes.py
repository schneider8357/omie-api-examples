import json
import os
from dotenv import load_dotenv
import omie

load_dotenv()

empresa = "CAV"

app_key = os.getenv(empresa + '_KEY')
app_secret = os.getenv(empresa + '_SECRET')


data = {
    "nPagina": 1,
    "nRegPorPagina": 100,
    "dDtInicial": "01/03/2024",
    "cHrInicial": "00:00:00",
    "cEtapa": 20,
}

res = omie.get(omie.listar_etapas_pedido, data, app_key, app_secret)

etapas_pedido = {e["cNumero"]: e for e in res["etapasPedido"]}

pedidos_marco = [
    {
        "data_etapa": p["dDtEtapa"],
        "etapa": "Aprova\u00e7\u00e3o do Financeiro",
        "numero_pedido": p["cNumero"],
        # "codigo_pedido": p["nCodPed"],
    } for p in etapas_pedido.values()
]

pedidos_marco_completos = []
for p in pedidos_marco:
    dados_pedido = omie.get(omie.consultar_pedido, {"numero_pedido": p["numero_pedido"]}, app_key, app_secret)
    valor_mercadorias = dados_pedido["pedido_venda_produto"]["total_pedido"]["valor_mercadorias"]
    infos_pedido = dados_pedido["pedido_venda_produto"]["informacoes_adicionais"]
    codigo_vendedor = infos_pedido["codVend"]
    vend = omie.get(omie.consultar_vendedor, {"codigo": infos_pedido["codVend"]}, app_key, app_secret)
    proj = omie.get(omie.consultar_projeto, {"codigo": infos_pedido["codProj"]}, app_key, app_secret)
    p["vendedor"] = vend["nome"]
    p["valor_mercadorias"] = valor_mercadorias
    p["projeto"] = proj["nome"]
    pedidos_marco_completos.append(p)