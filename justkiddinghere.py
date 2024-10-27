#lets rewind password project

import random
import string

pass_len = 12
x = string.ascii_letters + string.ascii_lowercase + string.digits + string.ascii_uppercase


password = ""              
for i in range(pass_len):
    password += random.choice(x)
    print("password is\n ",password)


