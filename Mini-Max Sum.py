def miniMaxSum(arr):
    minv= min(arr)                 # This line calculates the minimum value in the list 'arr' and assigns it to the variable 'minv'. 
    maxv= max(arr)                 # This line calculates the maximum value in the list 'arr' and assigns it to the variable 'maxv'. 
    sumv= sum(arr)                 # This line calculates the sum of all the elements in the list 'arr' and assigns it to the variable 'sumv'.
    print(sumv-maxv, sumv-minv)   
