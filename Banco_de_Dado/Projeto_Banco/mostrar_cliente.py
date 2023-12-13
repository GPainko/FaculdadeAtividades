import tkinter as tk
import mysql.connector

# Conectar ao banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="81107984",
    database="monitoramento"
)

# Cursor para executar operações no banco de dados
cursor = db.cursor()

# Função para obter e exibir clientes do banco
def show_clients():
    # Consulta para obter todos os clientes
    cursor.execute("SELECT * FROM cliente")
    results = cursor.fetchall()

    # Limpar a exibição anterior
    for widget in frame_clients.winfo_children():
        widget.destroy()

    # Exibir os clientes na interface gráfica
    for row in results:
        label_client = tk.Label(frame_clients, text=row)
        label_client.pack()

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Visualizador de Clientes do Banco de Dados")

# Botão para mostrar clientes
btn_show_clients = tk.Button(root, text="Mostrar Clientes", command=show_clients)
btn_show_clients.pack()

# Frame para exibir clientes
frame_clients = tk.Frame(root)
frame_clients.pack()

# Rodar a aplicação
root.mainloop()
