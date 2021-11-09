def bubble_sort(lista): 
    cC = 0
    cT = 0
    elementos = len(lista)-1 
    ordenado = False 
    while not ordenado: 
        ordenado = True 
        for i in range(elementos):
            cC += 1
            if lista[i] > lista[i+1]:
                cT += 2
                lista[i], lista[i+1] = lista[i+1],lista[i] 
                ordenado = False
    return [cC, cT]