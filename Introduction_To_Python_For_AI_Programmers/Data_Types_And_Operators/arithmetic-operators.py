#!/usr/bin/env python
# coding: utf-8

# > For solutions, check out the **arithmetic-operators-solution.ipynb** notebook in the current workspace. 
# 
# 
# # Quiz 1: Electricity bills 
# 
# My electricity bills for the last three months have been `$23`, `$32` and `$64`. What is my average monthly electricity bill over the three month period? 
# 
# Write an expression to calculate the mean,

# In[1]:


# Calculate the average of my utility bills for the past three months.
avg = (23+32+64)/3 #replace `None` with your code
print(avg)


# # Quiz 2: Tiles
# 
# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is **9 tiles wide by 7 tiles long**, the other is **5 tiles wide by 7 tiles long**. Tiles come in packages of 6.
# 
# 1. How many tiles are needed? 
# 2. You buy **17 packages of tiles containing 6 tiles each**. How many tiles will be left over?

# In[1]:


tiles = 17*6 #replace `None` with your code
used_tiles = 9*7 + 5*7
print(used_tiles)


# In[5]:


leftover_tiles = tiles - used_tiles #replace `None` with your code
print(leftover_tiles)



# In[ ]:




