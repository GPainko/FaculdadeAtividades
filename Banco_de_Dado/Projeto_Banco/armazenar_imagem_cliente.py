import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import StringVar
from PIL import Image
from PIL import ImageTk
import mysql.connector
import datetime

# Função para formatar CPF
def formatar_cpf(entry):
    cpf = entry.get()
    
    # Se o CPF estiver vazio, não faça nada
    if not cpf:
        return

    cpf = cpf.replace(".", "").replace("-", "")

    # Remova os zeros à esquerda desnecessários antes de preencher com zeros à esquerda novamente
    cpf = str(int(cpf))

    if len(cpf) < 11:
        cpf_formatado = cpf.zfill(11)
    else:
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    entry.delete(0, tk.END)
    entry.insert(0, cpf_formatado)

# Função para validar o CPF
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    return len(cpf) == 11 and cpf.isdigit()

# Conectar ao banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="81107984",
    database="monitoramento"
)

# Cursor para executar operações no banco de dados
cursor = db.cursor()

# Função para salvar imagem e horário no banco de dados
def save_image(filepath, timestamp):
    with open(filepath, "rb") as file:
        binary_data = file.read()
    cursor.execute("INSERT INTO imagens (imagem, horario) VALUES (%s, %s)", (binary_data, timestamp))
    db.commit()

# Função para carregar imagem
def upload_image():
    filepath = filedialog.askopenfilename()
    if filepath:
        timestamp = datetime.datetime.now()
        save_image(filepath, timestamp)

# Função para cadastrar pessoa
def register_person(name, cpf, location, num_cameras):
    cursor.execute("INSERT INTO cliente (nome, cpf, localizacao, numero_cameras) VALUES (%s, %s, %s, %s)",
                   (name, cpf, location, num_cameras))
    db.commit()

# Função para validar e formatar CPF ao perder o foco
def validate_cpf(event):
    entry = event.widget
    cpf = entry.get()
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido.")
        entry.delete(0, tk.END)
    else:
        formatar_cpf(entry)

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Sistema de Cadastro de Imagens e clientes")

# Botão para carregar imagem
btn_upload = tk.Button(root, text="Carregar Imagem", command=upload_image)
btn_upload.pack()

# Campos para cadastro de pessoas
label_name = tk.Label(root, text="Nome:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_cpf = tk.Label(root, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(root)
entry_cpf.pack()

# Adiciona uma variável de controle para o Entry do CPF
cpf_var = StringVar()
entry_cpf.config(textvariable=cpf_var)

# Adiciona validação de CPF ao perder o foco
entry_cpf.bind("<FocusOut>", validate_cpf)

label_location = tk.Label(root, text="Localização:")
label_location.pack()
entry_location = tk.Entry(root)
entry_location.pack()

label_num_cameras = tk.Label(root, text="Número de Câmeras:")
label_num_cameras.pack()
entry_num_cameras = tk.Entry(root)
entry_num_cameras.pack()

# Função para capturar dados do formulário e chamar o registro
def on_register():
    name = entry_name.get()
    cpf = entry_cpf.get()
    location = entry_location.get()
    num_cameras = entry_num_cameras.get()
    register_person(name, cpf, location, num_cameras)

# Botão para registrar pessoa
btn_register = tk.Button(root, text="Registrar cliente", command=on_register)
btn_register.pack()

# Rodar a aplicação
root.mainloop()
