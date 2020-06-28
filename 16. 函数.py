# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
 
#  不可写函数
# def ChangeInt( a ):
#     a = 10
 
# b = 2
# ChangeInt(b)
# print(b)    # 结果是 2



# 可写函数
# def changeme( mylist ):
#    mylist.append([1,2,3,4])
#    print("函数内取值: ", mylist)
#    return

# mylist = [10,20,30]
# changeme( mylist )
# print("函数外取值: ", mylist)


# 不顺序参数
# def printinfo( name, age ):
#    # "打印任何传入的字符串"
#    print("Name: ", name)
#    print("Age ", age)
#    return
 
# printinfo( age=50, name="miki" )


# 不定长参数
# def printinfo( arg1, *vartuple ):
#    # "打印任何传入的参数"
#    print(arg1)
#    for var in vartuple:
#       print(var)
#    return
 
# printinfo( 70, 60, 50 )


# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1,2))

