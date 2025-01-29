list = [1,2,3,4,5,6,7,8,9,8,5]
i = len(list) - 1
unique_nums = set()

while i >= 0:
    if list[i] not in unique_nums:
        unique_nums.add(list[i])
        print(list[i])
    i -= 1
