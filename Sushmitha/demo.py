print('hello')

a, b, c = 5, "sushmitha", 6.8
print('a = ', a)
print('b = ', b)
print('c = ', c)
print(type(b))
print(type(c))

#list

bts = ['rm' , 'jin', 'jhope', 'suga' , 'jimin' , 'v' ,'jk']
print('3rd name in bts_list is' , bts[2])
print('last name in bts_list is '+  bts[-1])     # string concadination
bts.insert(0 , 'kpop')   # adding_values
print(bts)
bts.append(7)    # adding_values
bts.append('end')
print(bts)
bts[-4] = 'KIM_TAEHYUNG'  # updating_values
print(bts)
del bts[-2]
print(bts)
print(bts[-4:-1])

#tuple

info = (8, 6, 'grey', 'red' ,3, 'green')
print(info)

#dict

dict ={'sushmitha':6, 8:'god', 'it':'at'}
print(dict)
print(dict[8])
print(dict['it'])
print(dict['sushmitha'])   # adding key & value
dict['is'] = 'was'
print(dict)

#if_else condition

we = 2
print('we value is ',we)
if we>4:
    print('we is greater')
elif we==0:
    print('we is 0')
else:
    print('we is smaller')

#for_loop

t = 5
for i in range(1, 10, 2):
    print(i*t)

#while_loop

print('while loop')
t = 8
while t>2:
    if t==7:
        t=t-1
        continue
    if t==3:
        break
    print(t)
    t=t-1
