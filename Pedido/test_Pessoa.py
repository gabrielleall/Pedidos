class Pessoa:
    def __init__(self):
        self.__Nome = None
        self.__Data_Nascimento = None
    
    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self,nome):
        self.__Nome = nome
    @property
    def Data_Nascimento(self):
        return self.__Data_Nascimento
    @Data_Nascimento.setter
    def Data_Nascimento(self,data):
        self.__Data_Nascimento = data
    def Calcular_Idade(self):
        return 2017 - self.__Data_Nascimento


class Cliente(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__Limite_Credito = None
        self.__Cartao_Credito  = None
        self.__Contato = None 
        self.__Status = None


    @property
    def Limite_Credito(self):
        return self.__Limite_Credito
    @Limite_Credito.setter
    def Limite_Credito(self,limite):
        self.__Limite_Credito = limite
    @property
    def Cartao_Credito(self):
        return self.__Cartao_Credito
    @Cartao_Credito
    def Cartao_Credito(self,nome_cartao):
        self.__Cartao_Credito = nome_cartao
    @property
    def Contato (self):
        return self.__Contato
    @Contato.setter
    def Contato(self,nome_contato):
        self.__Contato = nome_contato
    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self,status):
        self.__Status = status
    
    def Verificar_Credito(self):
        if self.__Limite_Credito > 0:
            print('Saldo Positivo')
        else:
            print('Saldo Negativo')
    def Validar_Cartiao(self):
        if self.__Status == 'Ok':
            print('Cartão Valido')
        else:
            print('Cartão Invalido')



pessoa = Pessoa()
pessoa.Nome = 'Renato'
pessoa.Data_Nascimento = 1993
print(pessoa.Calcular_Idade())
print(pessoa.Nome)
print(pessoa.Data_Nascimento)

'''
def test(self):
    pessoa = Pessoa()
    assert pessoa.Nome('Renato') == 'Renato'
    assert pessoa.Data_Nascimento('1993') == '1993'''
