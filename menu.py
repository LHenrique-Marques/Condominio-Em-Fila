from fila_espera import *
from lista_vagas import *



fila_espera = Fila()
lista_vagas_garagem = Lista()


def cadastrar_apartamentos():
    if len(torres) == 0:
        print("Erro!")
        print("Precisam de torres cadastradas para cadastrar apartamentos.")
        return
    else:
        novo_ap = Apartamento()
        novo_ap.cadastrar()
        if lista_vagas_garagem.tamanho < 10:
            lista_vagas_garagem.adicionar(novo_ap)
        else:
            fila_espera.adicionar(novo_ap)
        print("apartamento cadastrado.")
        novo_ap.imprimir()
        return

def cadastrar_torres():
    nova_torre = Torre()
    nova_torre.cadastrar()
    print("torre cadastrada.")
    nova_torre.imprimir()



def liberar_vaga():
    if lista_vagas_garagem.tamanho == 0:
        print("Não existem vagas para serem liberadas.")
        return
    while True:
        try:
            vaga_excluida = int(input("Informe o numero da vaga que deseja liberar: "))
            if 1 <= vaga_excluida <= 10:
                vaga_ocupada = False
                auxiliar = lista_vagas_garagem.inicio
                while auxiliar:
                    if auxiliar.vaga == vaga_excluida:
                        vaga_ocupada = True
                        break
                    auxiliar = auxiliar.proximo 
                if vaga_ocupada:
                    break
                else:
                    print("Vaga inexistente.")
                    return
            else:
                print("Digite um numero entre 1 e 10.")
        except:
            print("Digite um numero valido.")
    ap_excluido = lista_vagas_garagem.excluir(vaga_excluida)
    if fila_espera.tamanho > 0:
        ap_que_vai_receber_vaga = fila_espera.inicio
        fila_espera.remover()
        lista_vagas_garagem.adicionar(ap_que_vai_receber_vaga)
    fila_espera.adicionar(ap_excluido)

def ver_lista():
    lista_vagas_garagem.imprimir()

def ver_fila():
    fila_espera.imprimir()

def menu():
    while True:
        print("""
        ------------------------------------------------------
                                  MENU
        --------------------------------------------------------
        SELECIONE: 
        1 CADASTRAR TORRE
        2 CADASTRAR APARTAMENTO
        3 LIBERAR VAGA DA GARAGEM
        4 VER FILA DE ESPERA
        5 VISUALIZAR LISTA DA GARAGEM
        6 SAIR
        ---------------------------------------------------------""")

        try:
            escolha = int(input("Escolha uma opção.. "))
            if escolha == 1:
                cadastrar_torres()
            
            elif escolha == 2:
                cadastrar_apartamentos()
            elif escolha == 3:
                liberar_vaga()
            elif escolha == 4:
                ver_fila()
            elif escolha == 5:
                ver_lista()
            elif escolha == 6:
                    break
                
        except:
            print("Digite um numero valido...")




