
# coding: utf-8

# In[ ]:


import random

#creating number
randNum = random.randrange(0,20)
# flag variable
gues = False

#checking a number it will be runing till condition true

while gues==False:
    #input from users and int converts input into integer
    Input = int(input("Your guess please: "))
    
    #check if random nuber are equal or not
    if Input == randNum:
        gues = True
        score=100
        print("Congratulation You have Won")
    #check rang of input number
    elif Input > 20:
        print("Please try a bit lower  provide Number from 0 to 20")
    elif Input < 0:
        print("Please try a bit higher Negative Number could not be checked")
    elif Input >  randNum:
        print("Try a bit lower")
    elif Input < randNum:
        print("Try a bit higher")

print("End of program")

