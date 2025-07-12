import pyodbc

try:
    string_conexao = 'Driver= {ODBC Driver 17 for SQL Server}; Server=CNAT391788\SQLEXPRESS; Database=northwind; UID=sa; PWD=12345;'

    conexao = pyodbc.connect(string_conexao)
    print("Conexão bem-sucessida!")


    cursor = conexao.cursor()
    cursor.execute('SELECT ProdutoID, NomeProduto, PrecoUnitario from Produtos')
    registros = cursor.fetchall()
    for reg in registros:
        print(f'ID: {reg[0]}; Nome: {reg[1]}; Preço: {reg[2]}')
    print()


    cursor = conexao.cursor()
    cursor.execute('SELECT CategoriaID, NomeCategoria from Categorias')
    registros = cursor.fetchall()
    for reg in registros:
        print(f'ID: {reg[0]}; Nome: {reg[1]}')
    print()

    cursor.execute('CREATE TABLE AAAAAAAA(id int identity not null, descricao varchar(10) not null, primary key(id))')
    conexao.commit

except Exception as err: 
    print(f"Erro BD: {err}")