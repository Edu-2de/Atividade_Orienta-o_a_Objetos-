from produto import Produto



class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria  # Atributo fortemente privado

   
    def getTempoDeBateria(self):
        return self.__tempoDeBateria

   
    def setTempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        info = super().getInformacoes()
        return f"{info}, Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        return f"Notebook cadastrado: {self.getInformacoes()}"