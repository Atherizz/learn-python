def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    
def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
            
def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("items in the file:")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print("file not found")
        
        
count_words_and_lines("sialan.txt")
lirik = ["jancok", "memek", "jembud"]
write_item_to_file("sialan.txt", lirik)
read_items_from_file("sialan.txt")