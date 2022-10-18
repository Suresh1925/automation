#list is mutable
list_value = [1,2,"Hello",4,5]
#LIST is a datatype which allowes to store multiple values
print(list_value[0])
print(list_value[2])
print(list_value[-1]) 
print(list_value[1:3]) #will print last index-1

list_value.insert(3,"World")
print(list_value)

list_value.append(9) #This will add values at last 
print(list_value)

#To update a new value insted of old value
list_value[3]="GCIT"
print(list_value)

#To delete a value
del list_value[0]
print(list_value)

