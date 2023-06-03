def vasia(array):
    min_num = min(array)
    max_num = max(array)
    for i in range(len(array)):
        if array[i] == max_num:
            array[i] = min_num
    return array

n = int(input())
list_1 = [int(i) for i in input().split()][:n]
print(*vasia(list_1))