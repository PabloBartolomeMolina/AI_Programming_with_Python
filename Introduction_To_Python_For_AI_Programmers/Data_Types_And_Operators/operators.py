#!/usr/bin/env python
# coding: utf-8

# In[1]:


sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that gives a boolean value True if San Francisco is denser than Rio, and False otherwise
comparison_result = san_francisco_pop_density > rio_de_janeiro_pop_density #replace `None` with your code

### Notebook grading
if comparison_result == False:
    print('Your comparsion is correct. Nice work!')
else:
    print('Your answer is wrong. Double check your comparsion and make sure your code provides a boolean - True or False.')


# In[ ]:




