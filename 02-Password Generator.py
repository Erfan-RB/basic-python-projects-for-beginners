#Password Generator
import random 
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

password = "".join(random.sample(total, length))

print("Your password is : " + password)
