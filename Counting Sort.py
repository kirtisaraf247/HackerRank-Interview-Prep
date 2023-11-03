def countingSort(arr):
    c=[0 for i in range(100)]
    for i in arr:
        c[i]+=1
    return c
