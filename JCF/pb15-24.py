#pb15
print('pb15')

#name = input()
name = 'test'
print('안녕하세요. 저는 ' + name + '입니다.')

#pb16
print('pb16')

#InputStr = input()
InputStr = 'testing'
print(InputStr[::-1])

#pb17
print('pb17')

#height = int(input())
height = 321
if height >= 150:
    print('YES')
else:
    print('NO')

#pb18
print('pb18')

#scores = input()
scores = '12 43 24'

scorelist = scores.split(' ')

changes = []
for i in scorelist:
    changes.append(int(i))

print(sum(changes)//3)
'''
total = 0
for i in scorelist:
    total += int(i)

avg = total/3
#/가 하나일 경우 float로 반환, //일 경우 int형으로 반환
'''

#pb19
print('pb19')

#input_num = input()
input_num = '2 10'
inputs = input_num.split(' ')

num = int(inputs[0])
co = int(inputs[1])
'''
result = 1
for i in range(0, co):
    result = result*num
print(result)
'''
print(num**co)
#**는 제곱연산이다.

#pb20
print('pb20')

#input_num = input()
input_num = '15 5'
inputs = input_num.split(' ')
#위와 같이 입력된 문자열을 자동으로 구분하여 숫자로 입력하려면 지능형 list사용하기
#ex) l = [int(i) for i in input_num.split(' ')]

divend = int(inputs[0])
divisor = int(inputs[1])

print(str(divend//divisor) + ' ' + str(divend%divisor))

#pb21
print('pb21')

#how to make a 'set'?

a = {1,2,3,4,5,6}
b = {}
c = set('pythonpython')
d = set(range(5))
e = set()

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))

#pb22,23은 단순상식문제라 생략

#pb24
print('pb24')

str = 'marytas df'

print(str.upper())
