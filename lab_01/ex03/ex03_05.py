numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

print("List:", numbers)
print("Dictionary:", counts)