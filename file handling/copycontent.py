def copy_content (filename1, filename2):
    listItems = []
    try:
        with open(filename1, "r") as file1:
            contents = file1.readlines()
            for content in contents:
                listItems += content
        with open(filename2, "w") as file2:
            for listItem in listItems:
                file2.write(listItem)
    except FileNotFoundError:
        print("File not found!")

copy_content("sialan.txt", "copysialan.txt")