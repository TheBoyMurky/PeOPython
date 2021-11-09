def insertion_sort(lista):
    cC = 0
    cT = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        k = i
        cC += 2
        while k > 0 and chave < lista[k - 1]:
            cT += 1
            lista[k] = lista[k - 1]
            k -= 1
        cT += 1
        lista[k] = chave
    return[cC, cT]