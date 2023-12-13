import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import io;

# Conectar ao banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="81107984",
    database="monitoramento"
)

# Cursor para executar operações no banco de dados
cursor = db.cursor()

# Função para abrir e exibir imagem do banco
def open_image():
    # Consulta para obter a última imagem do banco (altere conforme necessário)
    cursor.execute("SELECT imagem FROM imagens ORDER BY horario DESC LIMIT 1")
    result = cursor.fetchone()

    if result:
        # Resultado contém os dados binários da imagem
        image_data = result[0]

        # Crie uma imagem PIL a partir dos dados binários
        image = Image.open(io.BytesIO(image_data))

        # Exiba a imagem usando Tkinter
        image_tk = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=image_tk)
        label.image = image_tk  # Mantenha uma referência para evitar a coleta de lixo
        label.pack()
    else:
        print("Nenhuma imagem encontrada no banco de dados.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Visualizador de Imagem do Banco de Dados")

# Botão para abrir imagem
btn_open_image = tk.Button(root, text="Abrir Última Imagem", command=open_image)
btn_open_image.pack()

# Rodar a aplicação
root.mainloop()
