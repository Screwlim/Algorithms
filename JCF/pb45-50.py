#pb45
print('pb45-----------------------------------')
import time
#time은 1970이후부터 지금까지의 시간을 초단위로 반환
t= time.time()
print(int(t//(365*24*3600) + 1970))

#pb46
print('pb46-----------------------------------')
s = 0
for i in list(range(21)):
    for j in str(i):
        s += int(j)

print(s)

#pb47
print('pb47-----------------------------------')

people = [
    ('a', '01033333333'),
    ('b', '01011111111'),
    ('c', '01022222222'),
    ('d', '01044444444'),
    ('a', '01033333333'),
    ('b', '01011111111'),
    ('c', '01022222222'),
    ('a', '01033333333'),
    ('b', '01011111111'),
    ('c', '01022222222'),
    ('d', '01044444444'),
    ('e', '01055555555')
]

#기존에 list로 선언되어 있던 자료형을 set으로 변형시키면서 중복을 제거
print(type(people))
print(len(set(people)))

#pb48
print('pb48-----------------------------------')
s = input()
result = []

for i in s:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())

print(''.join(result))#str로 변환하여 출력

#pb49
print('pb49-----------------------------------')

user_input = list(map(int, input().split()))
print(user_input)
print(max(user_input))
#list내에 정수형으로 넣어둔 후 max 내장함수 이용하여 최대값 구하

'''
#pb50
print('pb50-----------------------------------')

def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
            print(data[i], end= " ")

n = int(input())

data =  list(map(int, input().split()))

bubble(n, data)
'''