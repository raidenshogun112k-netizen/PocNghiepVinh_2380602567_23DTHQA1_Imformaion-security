student = {
    "name": "Vinh",
    "age": 20,
    "major": "Information Security"
}

print("Dictionary:", student)

key = input("Enter key to delete: ")

if key in student:
    del student[key]
    print("Dictionary after deletion:", student)
else:
    print("Key not found")