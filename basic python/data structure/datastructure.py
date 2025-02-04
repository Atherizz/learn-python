#LIST
bapak = ["agus", "roni", "budi", "bambang"]
bapak.append("drajat")
bapak.insert(2, "huda")
del bapak[0]

print(bapak)

bapak.pop()
print(bapak)
ambilBapak = bapak[1:3]
print(ambilBapak)

#TUPLE
color = ("red", "green", "blue")
print (color[-1])

#DICTIONARY
mhs = {"name" : "savero", "major" : "informatics engineering", "NIM" : "244107020116"}

mhs["ipk"] = 3.86
print(mhs)

del mhs["major"]
print (mhs["name"])

for key, value in mhs.items():
    print(key,value)
    
    if "major" in mhs:
        del mhs["major"]
    print(mhs)
    
#SETS
set1 = {1,2,3}
set2 = {3,4,5}

print("union : ", set1 | set2)
print("intersection : ", set1 & set2)