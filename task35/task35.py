def IsPrime(n):
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return 'no'
    return 'yes' 

n = int(input())
print(IsPrime(n))