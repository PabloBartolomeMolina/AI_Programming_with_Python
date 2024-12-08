#!/usr/bin/env python
# coding: utf-8

# # Quiz: Assign and Modify Variables
# 
# Now it's your turn to work with variables. The comments in this quiz (the lines that begin with `#`) have instructions for creating and modifying variables. After each comment write a line of code that implements the instruction.
# 
# Note that this code uses [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation) to define large numbers. `4.445e8` is equal to `4.445 * 10 ** 8` which is equal to `444500000.0`.

# In[7]:


# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6


# Use the multiplication assignment operator to decrease 
# the rainfall variable by 10% to account for runoff

rainfall = rainfall*.9


### Notebook grading
if rainfall == 5e6*.9:
    print("Nice job! You can use the multiplication assignment operator like this: rainfall *= .9")
elif rainfall == 5e6*1.1:
    print("Sorry! rainfall is too high. It looks like you increased rainfall by 10% instead of decreasing it.  Try again")        
else:
    print("Sorry! rainfall is incorrect.  Try again and make sure to use the *= assignment operator")


# In[8]:


# Use the addition assigment operator to add 
# the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall # rainfall keeps precedent value, rainfall*.9


### Notebook grading
if reservoir_volume == 5e6*.9 + 4.445e8:
    print("Nice job! You can use the multiplication assignment operator like this: reservoir_volume += rainfall")
elif reservoir_volume == 4.445e8:
    print("Sorry! reservoir_volume is too low. Did you add the rainfall?  Try again")        
else:
    print("Sorry! reservoir_volume is incorrect.  Try again and make sure to use the += assignment operator")


# In[9]:


# Use the multiplication assignment operator to increase 
# reservoir_volume by 5% to account for stormwater that 
# flows into the reservoir in the days following the storm

reservoir_volume *= 1.05 # reservoir_volume keeps precedent value, reservoir_volume += rainfall


### Notebook grading
if reservoir_volume == (5e6*.9 + 4.445e8)*1.05:
    print("Nice job! You can use the multiplication assignment operator like this: reservoir_volume *= 1.05")
elif reservoir_volume == 5e6*.9 + 4.445e8:
    print("Sorry! reservoir_volume is too low. Did you account for the stormwater?  Try again")        
else:
    print("Sorry! reservoir_volume is incorrect.  Try again and make sure to use the *= assignment operator")


# In[10]:


# Use the multiplication assignment operator to decrease 
# reservoir_volume by 5% to account for evaporation

reservoir_volume *= .95 # reservoir_volume keeps precedent value, reservoir_volume *= 1.05


### Notebook grading
if reservoir_volume == (5e6*.9 + 4.445e8)*1.05*.95:
    print("Nice job! You can use the multiplication assignment operator like this: reservoir_volume *= 0.95")
elif reservoir_volume == (5e6*.9 + 4.445e8)*1.05:
    print("Sorry! reservoir_volume is too low. Did you account for evaporation?  Try again")        
else:
    print("Sorry! reservoir_volume is incorrect.  Try again and make sure to use the *= assignment operator")



# In[11]:


# Use the subtraction assignment operator to subtract 
# 2.5e5 cubic metres from reservoir_volume to account 
# for water that's piped to arid regions.

reservoir_volume -= 2.5e5 # reservoir_volume keeps precedent value, reservoir_volume *= .95


### Notebook grading
if reservoir_volume == 447627500.0:
    print("Nice job! You can use the subtraction assignment operator like this: reservoir_volume -= 2.5e5")
elif reservoir_volume == (5e6*.9 + 4.445e8)*1.05*.95:
    print("Sorry! reservoir_volume is too high. Did you account for water that is piped to arid regions?  Try again")        
else:
    print("Sorry! reservoir_volume is incorrect.  Try again and make sure to use the -= assignment operator")


# In[ ]:




