'''
while
for
nested loop
'''

marks = [40,50,60,80,100]
num = 0
total = 0
while  num < 4:
    total = total + marks[num]
    num = num +1

print(total)

for x in marks:
    print(x)

students = [['mgmg',40,50,70],['aung aung',50,50,70]]

for temp1 in students:

    index = 1
    total = 0
    while index < 4:
        total = total + temp1[index]
        index += 1

    print('Nmae : '+temp1[0]+' Total Mark : '+str(total))
