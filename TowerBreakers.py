import os

def towerBreakers(n, m):
    if n % 2 == 0 or m == 1:         #Approach 1
        return 2
    else:
        return 1

    #return 2 if n % 2 == 0 or m == 1 else 1            #Approach 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
