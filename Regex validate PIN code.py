#!/usr/bin/env python
# coding: utf-8

# # Regex validate PIN code

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# 
# If the function is passed a valid PIN string, return true, else return false.
# 
# Examples

# "1234"   -->  true
# 
# "12345"  -->  false
# 
# "a234"   -->  false

# ## my solution

# In[1]:


def validate_pin(pin):
    
    pinlist= []
    
    for i in pin:
        if pin.isdigit():
            pinlist.append(i)
    
    if (len(pinlist)) == 4 or (len(pinlist)) == 6:
        return True
    else:
        return False


# In[ ]:




