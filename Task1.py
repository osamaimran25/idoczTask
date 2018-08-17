
# coding: utf-8

# In[57]:


def find_single_num(list1):
    num = 0
    #itrating over provided list
    for i in list1:
        #Xor opreation
        num ^= i
    return num

checkNum1 = [2,2,5,5, 3, 4,8,3, 4,8,9]
checkNum2 = [3, 2,1,6,5, 2, 1, 5, 3]
# checking function
print("single number in first list",find_single_num(checkNum1))
print("single number in 2nd list",find_single_num(checkNum2))

