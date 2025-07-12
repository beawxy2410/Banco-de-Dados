from django.shortcuts import render

import pyodbc


def home(request):
    try:
        # define os parametros de conexao
        driver   = '{ODBC Driver 17 for SQL Server}'
        servidor = '.\SQLEXPRESS'
        # servidor = 'localhost'
        banco    = 'northwind'
        usuario  = 'sa'
        senha    = 'Senha@123' # poder ser também: "senha", "senha@123", "Senha@123"

        # realiza conexao com o BD
        string_conexao = f'Driver={driver};Server={servidor};Database={banco};UID={usuario};PWD={senha}'
        conexao = pyodbc.connect(string_conexao)
        print("Conexão bem-sucedida!")

        # define um cursor para selecionar os registros de PRODUTOS
        cursor = conexao.cursor()
        cursor.execute('SELECT ProdutoID, NomeProduto, PrecoUnitario from Produtos')
        lista_produtos = cursor.fetchall()

        # reutiliza o cursor para selecionar os registros de CATEGORIAS
        cursor.execute('SELECT CategoriaID, NomeCategoria from Categorias')
        lista_categorias = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(
            request=request, 
            # pagina a ser carregada
            template_name='home.html', 
            # adiciona os dados das tabelas no "contexto"
            context={
                'produtos': lista_produtos, 
                'categorias': lista_categorias
            }
        )
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida na página 
    except Exception as err:
        return render(
            request=request, 
            template_name='home.html', 
            # adiciona a mensagem de erro no "contexto"
            context={'ERRO': err}
        )
