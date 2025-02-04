def specific_word_count(filename):
    specific_word = {}
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            for content in contents:
                words = content.split()
                for word in words:
                    if word in specific_word:
                        specific_word[word] += 1
                    else:
                        specific_word[word] = 1   
    except FileNotFoundError:
        print("File not found!")
    return specific_word

word_info = specific_word_count("sialan.txt")
print(word_info)
        
        