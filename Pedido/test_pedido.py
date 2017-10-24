class Produto:
    def __init__(self):
        self.__Nome_Produto = None
        self.__Peso = None
        self.__Qtd_Disponivel = None

    @property
    def Nome(self):
        return self.__Nome_Produto
    @Nome.setter
    def Nome(self,nome_produto):
        self.__Nome_Produto = nome_produto
    @property
    def Peso(self):
        return self.__Peso
    @Peso.setter
    def Peso(self,peso_produto):
        self.__Peso = peso_produto
    @property
    def Qtd_Disponivel(self):
        return self.__Qtd_Disponivel
    @Qtd_Disponivel.setter
    def Qtd_Disponivel(self,qtd_disponivel):
        self.__Qtd_Disponivel = qtd_disponivel

    def Consultar(self,produto):
        if self.__Nome_Produto == produto and self.__Qtd_Disponivel > 1:
            print ('{}: Produto Disposivel'.format(self.__Nome_Produto))
        elif self.__Nome_Produto == produto and self.__Qtd_Disponivel == 0:
            print ('{}: Produto Esgotado'.format(self.__Nome_Produto)
        else:
            print ('{}: Produto Indisponivel'.format(self.__Nome_Produto)

def test_pedido(self):
    assert 