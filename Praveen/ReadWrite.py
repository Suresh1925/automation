file = open('Test.txt')
#Read all content in the file
#print(file.read())
#print(file.read(2))

print(file.readline()) #read the 1st line #read one single line
print(file.readline()) #read the 2nd line


#Print line by line using readline method-100 lines
line = file.readline()
while line!="":
    print(line)
    line = file.readline()


file.close()  #memory leak , file corruption