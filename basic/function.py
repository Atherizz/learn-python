def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a-b

def divide(a,b):
    if (b!= 0):
        return a/b
    else:
        print("tidak bisa membagi 0!")
        
pilihan = int(input("masukkan pilihan 1 - 4:"))
        
num1 = float(input("masukkan angka ke-1 : "))
num2 = float(input("masukkan angka ke-2 : "))

match pilihan:
    case 1:
        print(add(num1,num2))
    case 2:
        print(substract(num1,num2))
    case 3:
        print(multiply(num1,num2))
    case 4:
        print(divide(num1,num2))
        




