import json
import os

from dotenv import load_dotenv

import omie

load_dotenv()

empresa = "CAV"

app_key = os.getenv(empresa + '_KEY')
app_secret = os.getenv(empresa + '_SECRET')

data = {
    'pagina': 1,
    'registros_por_pagina': 100,
}
res = omie.get(omie.listar_etapas_faturamento, data, app_key, app_secret)

try:
    print(json.dumps(res, indent=2))
except:
    print(res)
