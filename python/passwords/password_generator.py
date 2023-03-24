import random
import string
from random import *
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters)for x in range(randint(30, 30)))
print(password)
