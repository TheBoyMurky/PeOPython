from random import randint
from time import time
from prettytable import PrettyTable 

from QuickSort import quick_sort
from BubbleSort import bubble_sort
from SelectSort import select_sort
from InsertionSort import insertion_sort
from ShellSort import shell_sort

def gerar_lista(tamanho = 10):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, tamanho))
    return lista

def tempo_execucao(algoritmo, lista_desorganizado):

    

    inicio = time()
    if algoritmo == quick_sort:
        lista_contadores = algoritmo(lista_desorganizado, 0, len(lista_desorganizado) - 1)
    else:
        lista_contadores = algoritmo(lista_desorganizado)
    final = time()
    tempo_final = round((final - inicio), 4)
    print("Tempo de execução %.4f segundos" %tempo_final)
    return [tempo_final, lista_contadores]

def testar_algoritmos(tamanho_lista = 10):
    lista = []
    for i in range(5):
        lista.append(gerar_lista(tamanho_lista))
    print(f"Algoritmos com {tamanho_lista} elementos em um array")
    print("Quick Sort:")
    lista_cont_quick = tempo_execucao(quick_sort, lista[0])
    print("Bubble Sort:")
    lista_cont_bubble = tempo_execucao(bubble_sort, lista[1])
    print("Select Sort:")
    lista_cont_select = tempo_execucao(select_sort, lista[2])
    print("Insertion Sort:")
    lista_cont_insertion = tempo_execucao(insertion_sort, lista[3])
    print("Shell Sort:")
    lista_cont_shell = tempo_execucao(shell_sort, lista[4])
    
    tabela_testes = PrettyTable(["Algoritmo", "Tempo", "Comparações", "Trocas"])
    tabela_testes.add_row(["Quick Sort", lista_cont_quick[0], lista_cont_quick[1][0], lista_cont_quick[1][1]])
    tabela_testes.add_row(["Bubble Sort", lista_cont_bubble[0], lista_cont_bubble[1][0], lista_cont_bubble[1][1]])
    tabela_testes.add_row(["Select Sort", lista_cont_select[0], lista_cont_select[1][0], lista_cont_select[1][1]])
    tabela_testes.add_row(["Insertion Sort", lista_cont_insertion[0], lista_cont_insertion[1][0], lista_cont_insertion[1][1]])
    tabela_testes.add_row(["Shell Sort", lista_cont_shell[0], lista_cont_shell[1][0], lista_cont_shell[1][1]])
    print(tabela_testes)

if __name__ == "__main__":
    # testar_algoritmos()
    testar_algoritmos(1000)
    testar_algoritmos(10000)
    testar_algoritmos(100000)

    input()