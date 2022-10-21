txt_file = open('pycharm_sample.txt')
print(txt_file.read(15))   #print 1st 8 letters or 8byte in the file
print(txt_file.read())   #print full info in the file but starts from where the cursor is placed
print('read end')
txt_file.close()

with open('pycharm_sample.txt') as txt_file:     #other way to open txt file
    print(txt_file.readline())
    print(txt_file.readline())
    print('readline end')


txt_file = open('pycharm_sample.txt')
# f = txt_file.readline()
# while f!= '':
#     print(f)
#     f = txt_file.readline()
# print("end of readline while loop")

for f  in txt_file.readlines():     #using for loop lines are stored in default list form
    print(f)
print('end of readlines for loop')
