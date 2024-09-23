# file = open("mero_file.txt")
# contents = file.read()
#
# print(contents)
# file.close()

#to not use the close() method

with open("mero_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode = "w") as file:
    file.write("\nNew text")