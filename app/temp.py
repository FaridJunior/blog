# Python3 code to demonstrate working of 
# Converting String to binary 
# Using join() + ord() + format() 
print(ord('1'))
# initializing string 
test_str = "123"

# printing original string 
print("The original string is : " + str(test_str)) 

# using join() + ord() + format() 
# Converting String to binary 
res = ' '.join(format(ord(i)-48, 'b') for i in test_str) 

# printing result 
print("The string after binary conversion : " + str(res)) 
