greeting = "Good Morning"

if greeting=="morning":
    print("Condition Matched")
else:
    print("Condition Not Matched")
print("if else code is completed")

a = 3
if a>2:
    print("big num")
else:
    print("small num")

print("*****FOR LOOP*********")

obj=[11,22,33,44,55]
for i in obj:
    print(i)

#sum of 5 natural numbers
addition = 0
for i in range(1,6):
    addition = addition + i
print(addition) #15

#jump 2 iteration
for i in range(1,10,2):
    print(i)

for k in range(10): #skipping first index. It will start from zero.
    print(k)

print("*****WHILE LOOP*********")

t=4
while t>1:
    if t == 3:
        break
    print(t)
    t=t-1
print("While loop execution is done")

