# file = open("text.txt")
# print(file.read())
# print(file.read(2))
# file.close()
# print(file.readlines())
from turtledemo.chaos import line

with open("text.txt", "r") as reader:
    # print(reader.read())
    content = reader.readlines()
    print(content)
    reversed(content)
    #
    with open("text.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
            print(line)



# WRITE FILE

# with open("text.txt", "r") as reader:
