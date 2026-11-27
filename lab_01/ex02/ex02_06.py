X = int(input("Enter X: "))
Y = int(input("Enter Y: "))

array = []

for i in range(X):
    row = []

    for j in range(Y):
        row.append(i * j)

    array.append(row)

print(array)