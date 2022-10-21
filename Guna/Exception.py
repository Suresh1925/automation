ItemsInCart = 0
if ItemsInCart != 0 :
    pass

assert(ItemsInCart == 0)

# try and except

try:
    with open("test" , "r") as reader :
        reader.read()
except:
    print("I am custom except message")


try:
    with open("test" , "r") as reader:
        reader.read()

except Exception as e :
    print(e)

finally:
    print("this is for finally key word")