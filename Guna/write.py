with open("test" , "r") as reader :
    content =  reader.readlines()
    reversed(content)
    with open("test", "w") as writer :
        for line in reversed(content):
            writer.write(line)