
# coding: utf-8

# In[1]:


a = 15
b = 6
if a <b :
    print ("a Less than b")
elif a == b :
    print ("a equal b")
elif a>b +5:
    print ("a Greater than b by more than 5")
else :
    print ("a Greater than b")
    
print ("out side if")


# In[2]:


a = 15
b = 6
if a <b :
    print ("a Less than b")

else :
    if a == b :
        print ("a equal b")
    
    elif a>b +5:
        print ("a Greater than b by more than 5")
    else:
        print ("a Greater than b")
    
print ("out side if")


# In[3]:


hight_m=2
weight_kg=105
bmi = weight_kg/(hight_m**2)
if bmi<=25:
    print ("your bmi=")
    print (bmi)
else: 
    print ("over weight")

