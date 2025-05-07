from produto import Produto


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