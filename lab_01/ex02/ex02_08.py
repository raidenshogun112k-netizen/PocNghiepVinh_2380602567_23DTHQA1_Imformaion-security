numbers = input("Enter binary numbers: ").split(",")

result = []

for binary in numbers:
    decimal = int(binary, 2)

    if decimal % 5 == 0:
        result.append(binary)

print(",".join(result))