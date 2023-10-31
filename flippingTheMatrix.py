def flippingMatrix(matrix):
  sum = 0
 
  for i in range(n):
    for j in range(n):
    sum += max(matrix[i][j], matrix[i][~j], matrix[~i][j], matrix[~i][~j])
 
  return sum
