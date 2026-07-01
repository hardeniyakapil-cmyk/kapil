
#import random
#emp_name=["aman","kamal","shivam","anshu"]
#res=random.choice(emp_name)
#print(res)


#import random
#emp_name=["aman","kamal","shivam","anshu"]
#weight=[2,3,1,0]
#res=random.choices(emp_name,weights=weight,k=4)
#print(res)
#import random
#res=random.random()*10000
#print(int(res))
#import random
#rand_int=random.randint(1,10)
#rand_range=random.randrange(1,10)
#print(rand_int)
#print(rand_range)
#user max attempt=6
#each attempt random number generate.
#random number genrate sum.
#fix_value=150

#shuffle
#emp_name=["aman","kamal","shivam","anshu"]
#random.shuffle(emp_name)
#print(emp_name)
#coupon code
#CXYZ6755
#def generate_coupon():
   # a_to_z="abcdefghijklmnopqrstuvwxyz"
   # num="1234567890"

    #char=[random.choice(a_to_z)for i in range(1,5)]
    #num=[random.choice(num) for i in range(1,5)]

    #print("".join(char+num))

#for i in range(1,10):
   # generate_coupon()


# a_to_z="abcdefghijklmnopqrstuvwxyz"
   # num="1234567890"

#def generate_coupon():
 #   import string
  #  "".join(random.choices(string.ascii_uppercase ,k=4))
   # +"".join(random.choices(string.digits,k=4))

    #for i in range(10):
     #   generate_coupon()

#from datetime import datetime
#import time

#current=datetime.now().today()
#print(current)

#from datetime import datetime
#import time
#time.sleep(5)
#c=datetime.now()strftime()
#print(c)

import pyautogui
import time
time.sleep(4)
for i in range(100):
    pyautogui.typewrite("hello how are",interval=0.05)
    