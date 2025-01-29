import re

first = "Hello"
second = "world"
result = first + " " +  second
print(result)

text = "python programming"
print(text[0:6])
print(text[-11:])

print(f"{result} , im learning {text}" )

#split()
sentence = "python,is,suck"
words = sentence.split(",")
print(words)

#join() menggabungkan list kata yang telah di
new_sentence = " ".join(words)
print(new_sentence)

#replace()
text = "laravel cihuy"
updated_text = text.replace("laravel", "python")
print(updated_text)

#strip()
messy = "   Hello, World    "
cleaned_text = messy.strip()
print(cleaned_text)

