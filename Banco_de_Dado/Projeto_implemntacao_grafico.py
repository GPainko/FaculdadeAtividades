import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

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

# Configuração do banco de dados
config = {
    "host": "localhost",
    "user": "root",
    "password": "81107984",
    "database": "monitoramento"
}

# Estabelece a conexão com o banco de dados
try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Credenciais inválidas")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não encontrado")
    else:
        print(err)

# Cursor do banco de dados
cursor = db.cursor()

# Função para inserir dados no banco de dados
def inserir_dados(nome, cpf, localizacao, numero_cameras):
    try:
        cursor.execute("""
            INSERT INTO cliente (nome, cpf, localizacao, numero_cameras) 
            VALUES (%s, %s, %s, %s)
        """, (nome, cpf, localizacao, numero_cameras))
        db.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", str(err))
        db.rollback()

# Função chamada quando o botão salvar é pressionado
def on_salvar_pressed():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    localizacao = entry_localizacao.get()
    numero_cameras = entry_numero_cameras.get()
    
    if nome and cpf and localizacao and numero_cameras:
        inserir_dados(nome, cpf, localizacao, numero_cameras)
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_localizacao.delete(0, tk.END)
        entry_numero_cameras.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Cliente")

# Criando os campos de entrada (widgets)
label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_cpf = tk.Label(root, text="CPF:")
entry_cpf = tk.Entry(root)
entry_cpf_var = tk.StringVar()
entry_cpf["textvariable"] = entry_cpf_var
entry_cpf_var.trace_add("write", lambda name, index, mode, entry=entry_cpf: formatar_cpf(entry))

label_localizacao = tk.Label(root, text="Localização:")
entry_localizacao = tk.Entry(root)

label_numero_cameras = tk.Label(root, text="Número de Câmeras:")
entry_numero_cameras = tk.Entry(root)

button_salvar = tk.Button(root, text="Salvar", command=on_salvar_pressed)

# Organizar os widgets na janela
label_nome.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_cpf.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_cpf.grid(row=1, column=1, padx=5, pady=5)

label_localizacao.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_localizacao.grid(row=2, column=1, padx=5, pady=5)

label_numero_cameras.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_numero_cameras.grid(row=3, column=1, padx=5, pady=5)

button_salvar.grid(row=4, column=0, columnspan=2, pady=10)

# Executar a aplicação
root.mainloop()

# Fechar a conexão e cursor
cursor.close()
db.close()
