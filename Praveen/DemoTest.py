#list  same as array - should be in square bracket ( data can be updated)
values = [1, 2, "rahul", 4, 5] #variables #Hetro
print(values[0])
print(values[3])
print(values[-1]) #last index
print(values[1:3])
values.insert(3, "shetty")
print(values)
values.append("End") #adding value
print(values)
values[2] = "RAHUL"
del values[0]
print(values)

#tuple( data cannot be updated) round or parantheses
value=(1, 2, 'red', 3, 'blue')
print(value)



#dict = key/value pair form

dict = {"a": 13, 1: "DOB"}  # Key value pair
print(dict["a"])
print(dict[1])


