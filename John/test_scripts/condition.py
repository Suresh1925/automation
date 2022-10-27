John = "Good boy"
if John == "Goodboy":
    print("Condition matched")
elif John == "Good boy":
    print("Second Condition matched")
else: print("Condition not matched")

print ("***************************************")

# for loop
sim = ["kio", "vodamobile", "watertel", "jdea"]
for i in sim:
    print(i)
    # print(i[2])

print("***************************************")

num = [9, 5, 8, 0, 1, 2, 3]
for i in num:
    print(i/1)

print ("***************************************")

count = 0
for i in range(1,9):
    count = count + i
    print(i)
print("***************************************")
print(count)

print("3 arguements *****************************")

for l in range(1, 20, 3):
    print(l)

print("*****************************************")

for m in range (10):
    print("{}{}".format("value is",m))
