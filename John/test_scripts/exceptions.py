# Exception
itemsInCart = 0
if itemsInCart != 2:
    pass
assert (itemsInCart == 0)


# try catch
try:
    with open("filelog.txt", "r") as reader:
        reader.read()

 # automatically print exception msg, it prints the error automatically
except Exception as e:
    print(e)

# manually print exception msg
# except:
#     print("no files present in that name")

finally:
    print("Script passed or failed not a matter finally key is always gets triggered")