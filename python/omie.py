import os
import requests

'''
class Omie:
    def __init__(self, empresa):

        self.AlterarProduto = OmieAlterarProduto(empresa)
        self.ConsultarCliente = OmieConsultarCliente(empresa)
        self.ConsultarPedido = OmieConsultarPedido(empresa)
        self.ConsultarPedidoEtapas = OmieConsultarPedidoEtapas(empresa)
        self.ListarEtapasFaturamento = OmieListarEtapasFaturamento(empresa)
        self.ConsultarVendedor = OmieConsultarVendedor(empresa)
        self.ListarCenarios = OmieListarCenarios(empresa)
        self.ListarClientes = OmieListarClientes(empresa)
        self.ListarImpostosCenario = OmieListarImpostosCenario(empresa)
        self.ListarLocaisEstoque = OmieListarLocaisEstoque(empresa)
        self.ListarPosEstoque = OmieListarPosEstoque(empresa)
        self.ListarProdutos = OmieListarProdutos(empresa)
        self.ListarTabelaItens = OmieListarTabelaItens(empresa)
        self.ListarTabelasPreco = OmieListarTabelasPreco(empresa)

class OmieAlterarProduto:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = "AlterarProduto"
        self.codigo_produto = 0

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieConsultarCliente:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/clientes/"
        self.call = "ConsultarCliente"
        self.codigo_cliente_omie = 0
        self.codigo_cliente_integracao = ""

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieConsultarPedido:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/pedido/"
        self.call = "ConsultarPedido"
        self.codigo_pedido = 0

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieListarEtapasFaturamento:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/etapafat/"
        self.call = "ListarEtapasFaturamento"

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieConsultarPedidoEtapas:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/pedidoetapas/"
        self.call = "ListarEtapasPedido"

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieConsultarVendedor:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/vendedores/"
        self.call = "ConsultarVendedor"
        self.codigo = 0
        self.codInt = ""

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieListarCenarios:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/cenarios/"
        self.call = 'ListarCenarios'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieListarClientes:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/clientes/"
        self.call = 'ListarClientes'
        self.pagina = 1
        self.registros_por_pagina = 50

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

    def todos(self):
        nome_lista_omie = "clientes_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            produtos = self.executar()[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarImpostosCenario:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/cenarios/"
        self.call = 'ListarImpostosCenario'
        self.consumo_final = "N"
        self.codigo_produto = 0

    def executar(self):
        self.codigo_cliente_omie = OmieApi(self.empresa).cliente_imposto()
        self.codigo_cenario = OmieApi(self.empresa).cenario_imposto()
        return OmieApiCall().executar(self, self.empresa)

class OmieListarLocaisEstoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "estoque/local/"
        self.call = 'ListarLocaisEstoque'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

class OmieListarPosEstoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "estoque/consulta/"
        self.call = 'ListarPosEstoque'
        self.nPagina = 1
        self.nRegPorPagina = 20
        self.dDataPosicao = ""
        self.cExibeTodos = "N"
        self.codigo_local_estoque = OmieApi(empresa).local_de_estoque()

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

    def todos(self):
        nome_lista_omie = "produtos"
        self.nRegPorPagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['nTotPaginas']
        lista = consulta[nome_lista_omie]
        while self.nPagina < total_de_paginas:
            self.nPagina += 1
            produtos = self.executar()[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarProdutos:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = 'ListarProdutos'
        self.pagina = 1
        self.registros_por_pagina = 50
        self.apenas_importado_api = 'N'
        self.filtrar_apenas_omiepdv = 'N'

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

    def todos(self):
        nome_lista_omie = "produto_servico_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            produtos = self.executar()[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarTabelaItens:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = 'ListarTabelaItens'
        self.nPagina = 1
        self.nRegPorPagina = 20
        self.nCodTabPreco = 0
        self.cCodIntTabPreco = ""

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)

    def todos(self):
        nome_lista_omie = "listaTabelaPreco"
        self.nRegPorPagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['nTotPaginas']
        lista = consulta[nome_lista_omie]['itensTabela']
        while self.nPagina < total_de_paginas:
            self.nPagina += 1
            produtos = self.executar()[nome_lista_omie]['itensTabela']
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarTabelasPreco:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = 'ListarTabelasPreco'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApiCall().executar(self, self.empresa)
'''
consultar_pedido = "ConsultarPedido"
listar_etapas_pedido = "ListarEtapasPedido"
listar_etapas_faturamento = "ListarEtapasFaturamento"
consultar_vendedor = "ConsultarVendedor"
consultar_projeto = "ConsultarProjeto"
method_to_path = {
    consultar_pedido: 'produtos/pedido',
    listar_etapas_pedido: 'produtos/pedidoetapas',
    listar_etapas_faturamento: 'produtos/etapafat',
    consultar_vendedor: 'geral/vendedores',
    consultar_projeto: 'geral/projetos',
}

def get(method: str, data: dict, app_key: str, app_secret: str):
    json_data = {
        'app_key': app_key,
        'app_secret': app_secret,
        'call': method,
        'param': [data]
    }
    response = requests.post(f'https://app.omie.com.br/api/v1/{method_to_path.get(method)}/', json=json_data)
    try:
        return response.json()
    except:
        return response.text

