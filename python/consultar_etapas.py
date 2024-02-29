import json

from omie import *


exemplo = Omie("CAV").ListarEtapasFaturamento

exemplo.pagina = 1
exemplo.registros_por_pagina = 25
#exemplo.nCodPed = 1620

res = exemplo.executar()

try:
    print(json.dumps(res, indent=2))
except:
    print(res)
