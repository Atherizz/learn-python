def vokal_count(text):
    counter = 0
    for char in text.lower(): 
        if char in 'aiueo':
            counter += 1
    return counter

words = input("enter a words: ")
jumlah_vokal = vokal_count(words)
print(f"Jumlah vokal: {jumlah_vokal}")