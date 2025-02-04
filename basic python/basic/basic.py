print("hello world")

#DATA TYPE
lists = [1,2,3,4,6,7,8,9,10]
lists.append(5)
print(lists)
dict = {"name" : "savero", "major" : "informatics engineering"}
print(dict)
print(dict["name"])

#CONDITIONAL STATEMENT
age = 18
if age < 18 :
    print("enom")
else :
    print("tuek")
    
#LOOP

for list in lists:
    print(list)
    
for i in range(5):
    print(i)
    
while age > 5:
    print("oke")
    age -=1
    
#INPUT TEST & CONDITIONAL STATEMENT
num = int(input("masukkan angka : "))

if (num >1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
            print(f"{num} is a prime number")
else:
           print(f"{num} is not a prime number")