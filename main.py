from categoria import Categoria
from desktop_module import Desktop
from notebook import Notebook
import tkinter as tk
from tkinter import messagebox


def cadastrar_desktop():
    
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = entry_preco.get()
    potencia = entry_potencia.get()

    if not (modelo and cor and preco and potencia):
        messagebox.showerror("Erro", "Preencha todos os campos para cadastrar o Desktop.")
        return

    try:
        preco = float(preco)
        potencia = int(potencia)
    except ValueError:
        messagebox.showerror("Erro", "Preço e Potência devem ser numéricos.")
        return

    categoria = Categoria(1, "Desktop")
    desktop = Desktop(modelo, cor, preco, categoria, potencia)
    messagebox.showinfo("Cadastro de Desktop", desktop.cadastrar())


def cadastrar_notebook():
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = entry_preco.get()
    bateria = entry_bateria.get()

    if not (modelo and cor and preco and bateria):
        messagebox.showerror("Erro", "Preencha todos os campos para cadastrar o Notebook.")
        return

    try:
        preco = float(preco)
        bateria = int(bateria)
    except ValueError:
        messagebox.showerror("Erro", "Preço e Bateria devem ser numéricos.")
        return

    categoria = Categoria(2, "Notebook")
    notebook = Notebook(modelo, cor, preco, categoria, bateria)
    messagebox.showinfo("Cadastro de Notebook", notebook.cadastrar())



app = tk.Tk()
app.title("Cadastro de Produtos")


tk.Label(app, text="Modelo:").grid(row=0, column=0, padx=10, pady=5)
entry_modelo = tk.Entry(app)
entry_modelo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Cor:").grid(row=1, column=0, padx=10, pady=5)
entry_cor = tk.Entry(app)
entry_cor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Preço:").grid(row=2, column=0, padx=10, pady=5)
entry_preco = tk.Entry(app)
entry_preco.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Potência da Fonte (Desktop):").grid(row=3, column=0, padx=10, pady=5)
entry_potencia = tk.Entry(app)
entry_potencia.grid(row=3, column=1, padx=10, pady=5)

tk.Label(app, text="Tempo de Bateria (Notebook):").grid(row=4, column=0, padx=10, pady=5)
entry_bateria = tk.Entry(app)
entry_bateria.grid(row=4, column=1, padx=10, pady=5)


btn_desktop = tk.Button(app, text="Cadastrar Desktop", command=cadastrar_desktop)
btn_desktop.grid(row=5, column=0, padx=10, pady=10)

btn_notebook = tk.Button(app, text="Cadastrar Notebook", command=cadastrar_notebook)
btn_notebook.grid(row=5, column=1, padx=10, pady=10)


app.mainloop()