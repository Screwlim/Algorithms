
#pb31
print('pb31')

#pb32
print('pb32-----------------------------------')
instr = input().split(' ')
print(len(instr))

#pb33
print('pb33-----------------------------------')
innum = [int(i) for i in input().split(' ')]
for i in innum[::-1]:
    print(i, end=' ')


#pb34
print('pb34-----------------------------------')
heights = [int(i) for i in input().split(' ')]

'''
for i in range(0,len(heights)-1):
    if heights[i] > heights[i+1] :
        print('NO')
        break
'''
if heights != sorted(heights):
    print('NO')
else:
    print('YES')

#sort는 리스트의 내장함수로 객체를 정렬하고 (sort의 리턴값은 none)
#sorted는 받은 객체를 건드리지 않고 정렬된 값을 돌려준다.


#pb35
print('pb35-----------------------------------')

def one(n):
    def two(value):
        return value ** n
    return two

a = one(2)
b = one(3)
c = one(4)

print(a(10))
print(b(10))
print(c(10))
#factory에 대한 강의는 파이썬 강의 참고

#pb36
print('pb36-----------------------------------')
num = int(input())

for i in range(1, 10):
    print(num * i, end=' ')
