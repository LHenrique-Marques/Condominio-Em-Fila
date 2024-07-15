from apartamento import *

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, apartamento):
        if self.fim is None:
            self.inicio = apartamento
        else:
            self.fim.proximo = apartamento
        self.fim = apartamento
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            auxiliar = self.inicio
            self.inicio = auxiliar.proximo
            auxiliar.proximo = None
            self.tamanho -= 1
            if self.tamanho == 0:
                self.fim = None
        else:
            print("Lista vazia.")

    def imprimir(self):
        print("""
              ----------------------------------------
              Fila de espera por vaga
              ----------------------------------------
              """)
        if self.tamanho == 0:
            print("""
                  ------------------------------------
                  Lista vazia.
                  ------------------------------------
                  """)
            
            return
        else:
            numero_elementos = 1
            auxiliar = self.inicio
            
            while auxiliar:
                print(f"POSIÇÃO {numero_elementos}: {auxiliar}")
                auxiliar = auxiliar.proximo
                numero_elementos += 1
            print(f"""
                  -----------------------------------------------------------
                  {self.tamanho} apartamentos na lista de espera
                  -----------------------------------------------------------""")
            return
