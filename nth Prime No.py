x, y = map(int, input().split())
num = 2
count = 0
def prime(n):

    while True:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            count += 1
            if count == n:
                return num
            
            num += 1

    A = prime(x)
    B = prime(y)

    return A+B-1
            