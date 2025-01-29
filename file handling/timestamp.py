from datetime import datetime
current_time = datetime.now()
print(current_time.strftime("%d/%m/%Y %H:%M:%S"))

def log_with_timestamp(filename, message):
    current_time = datetime.now()
    try:
        with open(filename, "w") as file:
            file.write(f"{ message } ==> {current_time.strftime("%d/%m/%Y %H:%M:%S")}")
    except FileNotFoundError:
        print("File not found!")
        
log_with_timestamp("tes.txt", "halo cuy")