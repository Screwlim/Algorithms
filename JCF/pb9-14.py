#pb9
print('pb9')

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep = '/', end = ' ')
print(hour, minute, second, sep = ':')

#pb10
print('pb10')

print('type in the number of lines of the tree')
#treeheight = int(input())
treeheight = 4
'''
for i in range(1,treeheight+1):
    for k in range(0, treeheight-i):
        print(' ', end='')
    for j in range(1,i*2):
        print('*', end = '')
    print()
    ++i
'''
for i in range(1,treeheight+1):
    print(' ' *(treeheight-i) + '*'*(2*i-1))

print('tree done')

#pb11
print('pb11')

s = 0

for i in range(1, 101):
    s += i

print(s)

#pb12
print('pb12')

class Wizard():
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

#print(dir(x))

#pb13
print('pb13')

solar = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

planet = int(input())

print(solar[planet-1])

#pb14
print('pb14')

temp = int(input())

result = temp%3

if result == 0:
    print('짝')
else:
    print(temp)