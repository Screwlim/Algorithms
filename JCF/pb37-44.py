#pb37
'''
print('pb37-----------------------------------')
poll = input().split(" ")
count = 0

for i in range(1,len(poll)):
    if poll.count(poll[i-1]) < poll.count(poll[i]):
        res = i

print(poll[res] + '가 총 ' + str(poll.count(poll[res])) + '표로 반장이 되었습니다.')

#pb38
print('pb38-----------------------------------')
scores = [int(i) for i in input().split(' ')]
candy = 0

for i in range(3):
    top = max(scores)
    candy += scores.count(top)
    for j in range(scores.count(top)):
        scores.remove(top)
print(candy)

#pb39
print('pb39-----------------------------------')
l = input()
print(l.replace('q', 'e'))

#pb40
print('pb40-----------------------------------')
limit = int(input())
fnum = int(input())
onnum = 0
onboard = 0
for i in range(fnum):
    onboard += int(input())
    if onboard <= limit:
        onnum += 1

print(onnum)

#pb41
print('pb41-----------------------------------')
num = int(input())

for i in range(2,num):
    if num%i == 0:
        print('NO')
        break
    if i == num-1:
        print('YES')


#pb42
print('pb42-----------------------------------')
#라이브러리 활용을 할 수 있는가
import datetime
#요일은 weekday()로 0-6 = 일 - 토 순으로 반환
m = int(input())
d = int(input())

def Day(a, b):
    day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return day[datetime.date(2020, a, b).weekday()]

print(Day(m, d))

'''
#pb43
print('pb43-----------------------------------')

num = int(input())

res = []

while True:
    res.append(str(num%2))
    num = num//2
    if num == 1:
        res.append(str(1))
        break
'''
for i in range(len(res)-1, -1, -1):
    print(res[i], end='')
'''

res.reverse()
print(''.join(res))
#join을 활성화 하려면 res안에 있는 값이 다 str형이어야 함
#그러면 str == 모든 원소가 str형인 list?
#pb44
print('pb44-----------------------------------')
num = input()
total = 0
for i in num:
    total += int(i)

print(total)