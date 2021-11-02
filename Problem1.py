num = []
for i in range(1,1000):
    if i % 3 ==0 or i % 5==0:
        num.append(i)

print (num)
print (sum(num))