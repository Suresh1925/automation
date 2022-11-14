try: #control of try whenever it fails gets to except block)
  #  with open('Test.txt', 'r') as reader:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Some how i reached the block")

