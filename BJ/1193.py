num = int(input())

i = 1
while 1:
    if i*(i+1)//2 >= num:
        break
    else:
        i += 1

if i%2 == 0:
    ward = True
else:
    ward = False

if ward == True:
    a = num - i*(i-1)//2
    b = i - a + 1
else:
    b = num - i * (i - 1)//2
    a = i - b + 1

print(str(a) + '/' + str(b))