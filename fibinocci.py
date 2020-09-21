x = 0
y = 1
z = int(input("How many numbers?: "))  # Loop variable
z -= 2
print(x)
print(y)
while (z > 0):
    print(x + y)
    c = x + y
    x = y
    y = c
    z -= 1  # Decrement loop variable
