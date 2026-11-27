numbers = input("Enter list elements separated by spaces: ").split()

my_list = []

for number in numbers:
    my_list.append(int(number))

my_tuple = tuple(my_list)

print("List:", my_list)
print("Tuple:", my_tuple)