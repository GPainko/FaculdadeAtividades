import mysql.connector

# Estabelece a conexão com o banco de dados
db_config = {
    'user': 'root',
    'password': '81107984',
    'host': 'localhost',
    'database': 'monitoramento',
    'raise_on_warnings': True
}

db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

def inserir_cliente(nome, cpf, localizacao, numero_cameras):
    try:
        cursor.callproc('AddCliente', [nome, cpf, localizacao, numero_cameras])
        db_connection.commit()
        print('Cliente inserido com sucesso!')
    except mysql.connector.Error as err:
        print(f'Erro: {err}')


nome = input('Nome do Cliente:')
cpf = input('CPF do Cliente:')
bairro = input('bairro:')
n_camera = int(input('numero de camera Instaladas:'))


# inserção de cliente
inserir_cliente(nome,cpf, bairro,n_camera)

# Fecha a conexão
cursor.close()
db_connection.close()