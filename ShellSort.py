def shell_sort(arr):
    cC = 0
    cT = 0
    n = len(arr)
    gap = n/2
    while gap > 0:
        for i in range(int(gap), n):
            temp = arr[i]
            j = i
            cC += 2
            while j >= gap and arr[j - int(gap)] > temp:
                cT += 1
                arr[j] = arr[j - int(gap)]
                j -= int(gap)
            arr[j] = temp
        gap /= 2
    return[cC, cT]