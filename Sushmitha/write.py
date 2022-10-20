with open('pycharm_sample.txt', 'r') as reader:     #other way to open txt file with read mode
    info = reader.readlines()
    # print(info)
    reversed(info)
    with open('pycharm_sample.txt', 'w') as writer:    # other way to open txt file with write mode
        for line in reversed(info):
            writer.write(line)
            print(line)