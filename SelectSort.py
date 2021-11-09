def select_sort(array):
    cC = 0
    cT = 0
    length = len(array)
    for item in range(length):
        minimum = item
        for i in range(item + 1, length):
            cC += 1
            if array[i] < array[minimum]:
                minimum = i
        cT += 2
        (array[item], array[minimum]) = (array[minimum], array[item])
    return[cC, cT]
