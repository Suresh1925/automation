try:
    with open('file.txt', 'r') as reader:
        reader.read()
        print(reader)
except:
    print('file is not found so it cant read')

try:
    with open('file_log.txt', 'r') as reader:
        reader.read()
        print(reader)
except Exception as e:
    print(e)

finally:
    print('always execute')

