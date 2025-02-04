try:
    with open("sialan.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not Found")
    
print(content)