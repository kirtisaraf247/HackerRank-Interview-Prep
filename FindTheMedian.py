ef findMedian(arr):
 # Write your code here
 arr.sort()
 n= len(arr)
 if n% 2:
 return arr[n//2]
 else:
 return (arr[n//2-1]+arr[n//2])/2
