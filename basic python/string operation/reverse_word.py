def reverse_word(text):
    words = text.split(" ")

    for word in words:
        word = text[::-1]
        new_sentence = "".join(word)
        
    return new_sentence

sentence = input("enter a sentence : ")
print(reverse_word(sentence))