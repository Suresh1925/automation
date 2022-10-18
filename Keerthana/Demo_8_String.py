s = "Hello World"
s1 = ", GCIT"
s2 = "World"
print(s[1])
print(s[0:5]) # to get sub string #n-1
print(s+s1) #cancadination of string

print(s2 in s) # checkinh one string present in another string
# result will b True or False

# Split string 
var= s.split(" ")
print(var)

# To get 0th index
print(var[0])

# Strip
# This method is used to remove white space in the begninh and at the end
s3=" great "
print(s3)
print(s3.strip())
print(s3.lstrip()) #to remove space oly in left side l=left
print(s3.rstrip()) #to remove space only in left side r=right



