# read the file and store all the lines in list
#reverse the list
#write the reversed list back to the file


#to skip open() and close() command use following
from audioop import reverse


with open("test.txt",'r') as reader: # this code line will open and close the file 
    content = reader.readlines() #initial list
    reversed(content) # Reversed list
    with open("test.txt",'w') as writer:
        for line in reversed(content):
                writer.write(line)
                print(line)

