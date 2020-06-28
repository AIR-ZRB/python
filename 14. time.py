import time

# 获取时间戳
ticks = time.time()
print(ticks)

# 获取当前时间
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)


# 格式化日期
print(time.strftime("%Y-%m-%d"))

print(time.strftime("%H:%M:%S"))


# print(dir(time))