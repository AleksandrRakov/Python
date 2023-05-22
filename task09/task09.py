n = int(input("Нахождение N!: "))
x = 1
y = 1
while x <= n:
  y = y * x  # y *= y
  x = x + 1  # x += 1
print(f"{n}! = {y}")  