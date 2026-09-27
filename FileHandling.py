# open the file with relative path
file=open("input.txt", "a+")

# write into the file
file.write("\nThis is statement 2")
file.write("\nThis is statment 3")

# close the file
file.close()

file=open("input.txt", "r")

# read the content
content=file.read()
# close the file
file.close()
# print the content
print(content)