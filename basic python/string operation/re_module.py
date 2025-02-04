import re

text = "contact me at 0852-3534-2960"
digits = re.findall(r"\d+", text)
print(digits)

updated_text = re.sub(r"\d", "X", text)
print(updated_text)


def clean_text(text):
    #menghilangkan tanda baca
    text = re.sub(r"[^\w\s]", "", text)
    #menghilangkan spasi berlebihan
    text = " ".join(text.split())
    #convert to lowercase
    return text.lower()

def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    if text == text[::-1]:
        return True
    else:
        return False
    
def reverse_word(text):
    words = text.split(" ")

    for word in words:
        word = text[::-1]
        new_sentence = " ".join(word)
        
    return new_sentence
    
    
    
    


input_text = input("Enter a string: ")
check = is_palindrome(input_text)
print(f"{input_text} is a palindrom? {check}")


input_text = " Hello, World, !!! Welcome to Python, Programming...    "
cleaned_text = clean_text(input_text)
print("cleaned text :",cleaned_text)
    