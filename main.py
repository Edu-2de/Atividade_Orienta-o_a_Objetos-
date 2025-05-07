from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox
# Foi mal sor mandei errado ali de outra disciplina ksksksks.

# Classe Categoria
class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


# Classe abstrata Produto
class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Categoria: {self.categoria.nome}"

    @abstractmethod
    def cadastrar(self):
        pass


# Classe Desktop
class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte  # Atributo fracamente privado

    # Getter para potenciaDaFonte
    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte

    # Setter para potenciaDaFonte
    def setPotenciaDaFonte(self, potenciaDaFonte):
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        info = super().getInformacoes()
        return f"{info}, Potência da Fonte: {self._potenciaDaFonte}W"

    def cadastrar(self):
        return f"Desktop cadastrado: {self.getInformacoes()}"


# Classe Notebook
class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria  # Atributo fortemente privado

    # Getter para tempoDeBateria
    def getTempoDeBateria(self):
        return self.__tempoDeBateria

    # Setter para tempoDeBateria
    def setTempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        info = super().getInformacoes()
        return f"{info}, Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        return f"Notebook cadastrado: {self.getInformacoes()}"


# Interface gráfica usando tkinter
def cadastrar_desktop():
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = float(entry_preco.get())
    potencia = int(entry_potencia.get())
    categoria = Categoria(1, "Desktop")

    if modelo and cor and preco and potencia:
        desktop = Desktop(modelo, cor, preco, categoria, potencia)
        messagebox.showinfo("Cadastro de Desktop", desktop.cadastrar())
    else:
        messagebox.showerror("Erro", "Preencha todos os campos para cadastrar o Desktop.")


def cadastrar_notebook():
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = float(entry_preco.get())
    bateria = int(entry_bateria.get())
    categoria = Categoria(2, "Notebook")

    if modelo and cor and preco and bateria:
        notebook = Notebook(modelo, cor, preco, categoria, bateria)
        messagebox.showinfo("Cadastro de Notebook", notebook.cadastrar())
    else:
        messagebox.showerror("Erro", "Preencha todos os campos para cadastrar o Notebook.")


# Configuração da interface gráfica
app = tk.Tk()
app.title("Cadastro de Produtos")

# Labels e entradas
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

# Botões
btn_desktop = tk.Button(app, text="Cadastrar Desktop", command=cadastrar_desktop)
btn_desktop.grid(row=5, column=0, padx=10, pady=10)

btn_notebook = tk.Button(app, text="Cadastrar Notebook", command=cadastrar_notebook)
btn_notebook.grid(row=5, column=1, padx=10, pady=10)

# Loop da interface gráfica
app.mainloop()