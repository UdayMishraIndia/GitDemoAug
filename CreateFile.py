import os

os.makedirs("Test", exist_ok=True)

filePath = "Test/test.txt"

with open(filePath, "x") as file:
    file.writelines("\nHello Uday!")
    file.writelines("\nHow are you?")

with open(filePath, "r") as file:
    content=file.read()
    print(content)    
