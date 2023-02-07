# 更加简洁的Counter,使用生成器

def counter(start,stop):
    while start <= stop:
        yield start
        start += 1

for i in counter(101,105):
    print(i)