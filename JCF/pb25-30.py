#pb25
print('pb25')

r = 4

width = r*r*3.14
print(width)

#pb26
print('pb26')

solar = {'수성':'Mercury',  '금성':'Venus', '지구' :'Earth', '화성' : 'Mars', '목성':'Jupiter', '토성' : 'Saturn','천왕성':'Uranus','해왕성':'Neptune' }
planet = '지구'

print(solar.get(planet))

#pb27
print('pb27')

names = 'Yujin James Hyewon'
scores = '20 50 14'
namelist = names.split(' ')
scorelist = scores.split(' ')

dic = {}

for i in range(0,len(namelist)):
    dic[namelist[i]] = int(scorelist[i])

print(dic)
'''
순서가 알맞게 list두개를 설정후 zip()함수로 dic 생성

dic = dict(zip(namelist, scorelist))
'''


#pb28
print('pb28')

instr = 'python'

for i in range(1,len(instr)):
    print(instr[i-1] + instr[i])

#pb29
print('pb29')
inchar = 'S'

'''
python에서도 아스키코드 동일
단, c언어처럼 단순히 int와 char가 바로 출력/연산하는 자료형에 따라가는 것이 아님
ord() : 문자를 숫자로
char() : 숫자를 문자로
바꾸어 주는 함수를 사용해야 함.
단, 문자간 대소 비교는 가능
'''
if (inchar >= 'A') & (inchar <= 'Z'):
    print('YES')
else:
    print('NO')

#pb30
print('pb30')

instr = input()
findstr = input()

j = 0
init = 0
'''
for i in range(0, len(instr)):
    if findstr[j] == instr[i]:
        j += 1
        if j == len(findstr):
            print(i - j + 1)
            break
    elif findstr[0] == instr[i]:
        j = 0
        init = i
    else:
        j = 0

'''
#내장함수find() 사용하면 끝...
print(instr.find(findstr))