

def rev_num(n):
    if n == 0:
        return ''
    k = input()
    return rev_num(n - 1) + f' {k} '

n = int(input())
print(rev_num(n))