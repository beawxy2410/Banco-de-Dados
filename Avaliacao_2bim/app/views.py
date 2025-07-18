from django.shortcuts import render

import pyodbc


def obter_conexao():
    # define os parametros de conexao
    driver   = '{ODBC Driver 17 for SQL Server}'
    servidor = '.\SQLEXPRESS'
    banco    = 'Avaliacao_2bim'
    usuario  = 'sa'
    senha    = 'Senha@123' # poder ser também: "senha", "senha@123", "Senha@123" se for no lab06 "12345"

    # realiza conexao com o BD
    string_conexao = f'Driver={driver};Server={servidor};Database={banco};UID={usuario};PWD={senha}'
    conexao = pyodbc.connect(string_conexao)
    
    # retorna a conexao  
    return conexao


def home(request):
    # define a página HTML (template) que deverá será carregada
    template = 'home.html'
    return render(request, template)

def questao_3a(request):
    # define a página HTML (template) que deverá será carregada
    template = 'questao_3a.html'
    try:
        # obtem a conexao com o BD
        conexao = obter_conexao()

        # define um cursor para executar comandos SQL
        #cursor realiza comandos SQL e retornam para o código
        cursor = conexao.cursor()

        # define o comando SQL que será executado
        sql = '''
            SELECT	Produto.id,
                    	Produto.descricao,
		        Produto.valor_unitario,
		        Categoria.descricao AS descricao_categoria
                    
            FROM Produto
            INNER JOIN Categoria ON Produto.categoria_id = Categoria.id
            
            ORDER BY Categoria.descricao, Produto.descricao
        '''
        # usa o cursor para executar o SQL
        #excuta uma consulta sql
        cursor.execute(sql)
        # obtem todos os registros retornados
        #fetchall retorna todos os registros de uma tabela
        registros = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, template, context={'registros': registros})
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página 
    except Exception as err:
        return render(request, template, context={'ERRO': err})


def questao_3b(request):
    # define a página HTML (template) que deverá será carregada
    template = 'questao_3b.html'
    try:
        # obtem a conexao com o BD
        conexao = obter_conexao()

        # define um cursor para executar comandos SQL
        #cursor realiza comandos SQL e retornam para o código
        cursor = conexao.cursor()

        # define o comando SQL que será executado
        sql = '''
           SELECT   Venda.data_venda,
                    Venda.valor_total,
                    Produto.descricao AS descricao_produto,
                    Cliente.nome AS nome_cliente,
                    Vendedor.nome AS nome_vendedor
                    
            FROM Venda
            INNER JOIN Produto ON Venda.produto_id = Produto.id
            INNER JOIN Cliente ON Venda.cliente_id = Cliente.id
            INNER JOIN Vendedor ON Venda.vendedor_id = Vendedor.id

            ORDER BY Venda.data_venda DESC
        '''
        # usa o cursor para executar o SQL
        #excuta uma consulta sql
        cursor.execute(sql)
        # obtem todos os registros retornados
        #fetchall retorna todos os registros de uma tabela
        registros = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, template, context={'registros': registros})
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página 
    except Exception as err:
        return render(request, template, context={'ERRO': err})


