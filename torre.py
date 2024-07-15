torres = []

class Torre:

    id_contador = 1

    def __init__(self):
        self.id = Torre.id_contador
        self.nome = None
        self.endereco = None
        self.apartamentos = []
        Torre.id_contador += 1

    def escolhe_nome(self):
        while True:
            nome = input("Digite o nome da torre que ira cadastrar:   ").strip()
            if nome:
                self.nome = nome
                break
            else:
                print("Digite o nome valido:  ")

    def escolhe_endereco(self):
        while True:
            end = input("Digite o endereço:  ").strip()
            if end:
                self.endereco = end
                break
            else:
                print("Digite um endereço valido: ")

    def cadastrar(self):
        self.escolhe_nome()
        self.escolhe_endereco()
        torres.append(self)

    def __str__(self):
        return f"TORRE: {self.nome}, ENDEREÇO: {self.endereco}. ID: {self.id}"

    def imprimir(self):
        print(self)
