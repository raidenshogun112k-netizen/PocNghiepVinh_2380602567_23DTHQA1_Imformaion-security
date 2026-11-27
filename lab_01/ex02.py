import re

text = input("Nhập chuỗi: ")

numbers = re.findall(r'-?\d+', text)

positive_sum = 0
negative_sum = 0

for number in numbers:
    number = int(number)

    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number

print("Giá trị dương:", positive_sum)
print("Giá trị âm:", negative_sum)