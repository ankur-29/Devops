# Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is my first file write operation in Python!\n")
    file.write("This is another line.\n")

print("Data written successfully to example.txt")

# Reading from a File
with open("example.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)
