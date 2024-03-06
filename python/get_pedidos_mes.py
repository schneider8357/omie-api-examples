import json
import os

import pandas as pd
from dotenv import load_dotenv
import requests

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
    } for p in etapas_pedido.values()
]

print(f"encontrados {len(pedidos_marco)} pedidos com aprovação do financeiro em março")

pedidos_marco_completos = []
for p in pedidos_marco:
    dados_pedido = None
    vend = None
    proj = None
    valor_mercadorias = None
    resp = None
    dados_pedido = omie.get(omie.consultar_pedido, {"numero_pedido": p["numero_pedido"]}, app_key, app_secret)
    if "pedido_venda_produto" not in dados_pedido:
        print(f"erro nos dados do pedido {p=}: faltando chave 'pedido_venda_produto'\n{dados_pedido=}")
        continue
    p["valor_mercadorias"] = dados_pedido["pedido_venda_produto"]["total_pedido"]["valor_mercadorias"]
    if "informacoes_adicionais" not in dados_pedido["pedido_venda_produto"]:
        print(f"erro nas informações adicionais {p=}: faltando chave 'informacoes_adicionais'\n{dados_pedido=}")
        continue
    infos_pedido = dados_pedido["pedido_venda_produto"]["informacoes_adicionais"]
    if "codVend" in infos_pedido:
        p["vendedor"] = omie.get(omie.consultar_vendedor, {"codigo": infos_pedido["codVend"]}, app_key, app_secret).get("nome")
    else:
        print(f"erro nos dados do pedido {p=}: faltando chave 'codVend'")
    if "codProj" in infos_pedido:
        p["projeto"] = omie.get(omie.consultar_projeto, {"codigo": infos_pedido["codProj"]}, app_key, app_secret).get("nome")
    else:
        print(f"erro nos dados do pedido {p=}: faltando chave 'codProj'")
    p["cliente_nome"] = infos_pedido["contato"]
    p["cliente_email"] = infos_pedido["utilizar_emails"]
    pedidos_marco_completos.append(p)
    #if 'faultcode' in resp and resp['faultcode'] == 'SOAP-ENV:Client-107':
    #    print(f"pulando {p=}, codigo 50XXX")
    #    continue

df = pd.DataFrame(pedidos_marco_completos)
df.to_csv("pedidos_vendas_03_2024.csv")

