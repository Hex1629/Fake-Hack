import random
import time
import string
import sys
import os

print("\033[92mGenerator Password v1.0")
print("\033[0m")

name = string.ascii_lowercase
user = ''.join(random.choice(name) for i in range(8))

letter = string.ascii_lowercase + string.ascii_lowercase
pas = ''.join(random.choice(letter) for i in range(40))

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("\033[92mUser:", user,"\033[0m")
    print("\033[92mRandom password:", result_str,"\033[0m")
    txt = result_str
    x = pas in txt
    print("\033[92mPassword:",x,"\033[0m")

time.sleep(3)
print("\033[92mRun\033[0m")
time.sleep(0.2)
sent = 40
while True:
     os.system("clear")
     get_random_string(sent)
     time.sleep(0.9)