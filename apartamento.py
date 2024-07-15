from torre import *

numeros_apartamentos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

class Apartamento:

    id_contador = 1

    def __init__(self):
        self.id = Apartamento.id_contador
        self.numero = None
        self.torre = None
        self.vaga = None
        self.proximo = None        
        Apartamento.id_contador += 1

    def escolhe_numero(self):
        while True:
            try:
                num = int(input("Digite o numero do ap: "))
                if num in numeros_apartamentos:
                    if num in self.torre.apartamentos:
                        print("Este AP ja esta nessa torre.")
                    else:
                        self.numero = num
                        break
                else:
                    print("Numero invalido...")
            except:
                print("Digite um numero valido..")

    def escolhe_torre(self):
        print("""
           --------------------------------------------------
           Lista de torres cadastradas
           --------------------------------------------------   
              
              """)
        indice = 1
        for torre in torres:
            print(f"TORRE {indice}: {torre}. \n")
            indice += 1
        while True:
            try:
                id_torre = int(input("Digite o ID da torre: "))
                if id_torre > 0 and id_torre <= len(torres):
                    self.torre = torres[id_torre - 1]
                    break
                else:
                    print("Digite um ID valido..")
            except:
                print("Escolha um numero valido..")

    def cadastrar(self):
        self.escolhe_torre()
        self.escolhe_numero()
        self.torre.apartamentos.append(self.numero)

    def __str__(self):
        return f"AP {self.numero}, VAGA: {self.vaga}, TORRE: {self.torre.nome}. ID: {self.id}"

    def imprimir(self):
        print(self)
