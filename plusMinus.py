def plusMinus(arr):
    positive=0
    neg=0
    zero=0
    for i in arr:
        if i>0:
            positive+=1
        elif (i<0):
            neg+=1
        else:
            zero+=1
    n=len(arr)
    pp=positive/n
    np=neg/n
    zp=zero/n      
    print(round(pp,6))
    print(round(np,6))
    print(round(zp,6))
