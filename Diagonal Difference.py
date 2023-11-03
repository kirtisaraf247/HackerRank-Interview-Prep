def diagonalDifference(arr):
    n=len(arr)                  # The variable 'n' is assigned the value of the number of rows (or columns) in the matrix. 
    ls,rs = 0,0
    for i in range(n):          # THe 'for' loops with variables 'i' and 'j' ranging from '0' to 'n-1'. These loops are used to iterate over all the elements of the square matrix.
        for j in range(n):      
            if i==j:            # The first 'if' statement checks if 'i' is equal to 'j',
                ls+=arr[i][j]   # which means that the current element is on the left diagonal. If this condition is true, the element at (i, j) is added to 'ls'.
            if i+j ==n-1:       # The second 'if' statement checks if 'i + j' is equal to 'n-1', 
                rs+=arr[i][j]   # which means that the current element is on the right diagonal. If this condition is true, the element at (i, j) is added to 'rs'.
    return abs(ls-rs)           # The function returns this absolute diagonal difference as the result.
