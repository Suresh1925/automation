Group = [5, 78, 5.79854, "john", True]
Group2 = (4, 77, 5.7985, "ahul", False)
Group3 = {3, 76, 5.798, "hul", True}
Group4 = {"name":"Guna", "age":17}
Group5 = [5, 78, 5.79854, "john", True]
print(type(Group[4]))
print(Group2[2])
print(Group[-1])
print(Group[1:4])
Group.insert(4, "babu")
print(Group)
# Group5.append([4], "babu")
print(Group5)
print(Group4["name"])

print ("***************************************")


# Add values to dictionary
dict_Values={}
dict_Values["fname"] = "John"
dict_Values["lname"] = "babu"
dict_Values["age"] = 25
dict_Values["gender"] = "Male"
print(dict_Values)
print(dict_Values["age"])