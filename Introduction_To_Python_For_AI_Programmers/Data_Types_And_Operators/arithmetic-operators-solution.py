#!/usr/bin/env python
# coding: utf-8

# # Quiz 1: Electricity bills 
# 
# My electricity bills for the last three months have been `$23`, `$32` and `$64`. What is my average monthly electricity bill over the three month period? 
# 
# Write an expression to calculate the mean,

# In[1]:


# Calculate the average of my utility bills for the past three months.
avg = ((23+32+64)/3)
print (avg)


# # Quiz 2: Tiles
# 
# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is **9 tiles wide by 7 tiles long**, the other is **5 tiles wide by 7 tiles long**. Tiles come in packages of 6.
# 
# 1. How many tiles are needed? 
# 2. You buy **17 packages of tiles containing 6 tiles each**. How many tiles will be left over?

# In[2]:


tiles = (9*7 + 5*7)
print(tiles)


# In[3]:


leftover_tiles = ((17*6)-(9*7 + 5*7))
print(leftover_tiles)



# In[ ]:




