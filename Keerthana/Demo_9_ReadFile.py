file = open("test.txt", 'r') # to open and Read all the conetent of files 
# print(file.read(4)) # To read the file content

# To read single line of file line by line
# In previous code file already read till 4, So this will start reading after 4
# file.readline # This will read 1st line
# file.readline # This will read 2st line

# line = file.readline()
# while line != "": # When line not equal to blank
#     print(line)
#     line = file.readline() # after reading the line, line = empty
    
for line in file.readlines(): #readlines - to read multiple lines
    print(line)  




file.close()

