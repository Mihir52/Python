str = input("Enter string : ")
mid_str = input("Enter mid string : ")

findMid_part = len(str) // 2

last_str = str[:findMid_part] + mid_str + str[findMid_part:]

print(last_str)