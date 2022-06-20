#funtion imports
import string       
import random
# importing the valuses of the funtions in the strings
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
#combining the all the values from strings s1:s4 in  a list called s.
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print("//////////////WELCOME TO PASSWORD GENERATOR/////////////")
passlen = int(input("Enter the length if the password you want: "))
random.shuffle(s) #shuffles the list s in a random manner
print ("".join(s[0:passlen]))