n = 385916
num1 = n // 100000 # 100 000
num2 = (n % 100000) // 10000 # 10 000
num3 = (n % 10000) // 1000 # 1 000
num4 = (n % 1000) // 100 # 100
num5 = (n % 100) // 10 # 10
num6 = n % 10 # 1
res = num1 + num2 + num3
res2 = num4 + num5 + num6

if res == res2:
    print("yes")
else:
    print("no")