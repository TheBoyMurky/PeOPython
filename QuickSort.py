def partition(arr, low, high, cC, cT):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        cC += 1
        if arr[j] <= pivot:
            i = i+1
            cT +=2
            arr[i], arr[j] = arr[j], arr[i]
    cT += 2
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return [i+1, cC, cT]
  
  
def quick_sort(arr, low, high, cC = 0, cT = 0):
    if len(arr) == 1:
        return arr
    if low < high:
        part = partition(arr, low, high, cC, cT)
        pi = part[0]
        cC = part[1]
        cT = part[2]
        quick_sort(arr, low, pi-1, cC, cT)
        quick_sort(arr, pi+1, high, cC, cT)
    return [cC, cT]