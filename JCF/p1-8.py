#pb1
print('pb1')
nums = [100, 200, 300, 400, 500]

'''
nums.remove(400)
nums.remove(500)
'''
'''
del nums[3]
del nums[3]
'''
nums = nums[:3]


print(nums)
#pb2
print('pb2')
l = [200, 100, 300]
l.insert(2, 100000)
print(l)

#pb3
print('pb3')
l = [100, 200, 300]
print(type(l))
#class 'list'

#pb4
print('pb4')
a = 1
print(type(a))
#class 'int'
a = 2.22
print(type(a))
#class 'float'
a = 'p'
print(type(a))
#class 'str'
#char가 아님
a = [1, 2, 3, 4]
print(type(a))
#class 'list'

#pb5
print('pb5')

a = 10
b = 2
for i in range(1, 5, 2):
    a += 1

# a = 12, b = 2 즉 14
print(a+b)

#pb6
print('pb6')

print(bool(None))
print(bool(1))
print(bool(""))
print(bool(0))
print(bool(bool(0)))

#1 이상은 참이다.

#pb7
print('pb7')

#as는 예약어로 이미 지정되어 있고 변수명은 숫자로 시작할 수 없다.

#pb8
print('pb8')

d = {'height':180, 'weight':78, 'weight':84, 'temperature':36, 'eyesight':1}
print(d['weight'])

#같은키가 존재할 경우 가장 뒤에 있는 값을 출력