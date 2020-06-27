result = 0
i = 0

# 简单累加
# while i <= 10:
#     result += i 
#     i += 1

# print(result)
# print(i)

# 偶数求和
# while i < 100:
#     if (i % 2 == 0):
#         result += i
#     i += 1
    
# print(result)



# break退出循环
# while i < 5:
#     print(i)
#     if i == 2:
#         print("END")
#         break
#     i += 1


# continue退出循环
while i < 5:
    
    if i == 2:
        print("END")
        i += 1 
        continue
    print(i)
    i += 1

