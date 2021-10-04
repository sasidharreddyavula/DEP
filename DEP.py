#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


py = pd.read_csv("Nodes.csv")


# In[3]:


py.head()


# In[4]:


py.columns


# In[5]:


py.shape


# In[1]:


import pandas as pd
import numpy as np


# In[2]:


jp = pd.read_csv("Nodes.csv")


# In[3]:


jp.head()


# In[4]:


jp.shape


# In[5]:


jp.columns


# In[6]:


jp.BEGINBULK[0:10]


# In[7]:


jp.BEGINBULK[45:50]


# In[8]:


jp.BEGINBULK[1000:5000]


# In[9]:


jp.BEGINBULK[50000:60000]


# In[11]:


jp.columns


# In[12]:


jp.shape


# In[14]:


jp.BEGINBULK[1::]


# In[15]:


jp.BEGINBULK[::1]


# In[16]:


jp.BEGINBULK[1::5]


# In[17]:


jp.BEGINBULK[::-1]


# In[18]:


jp.BEGINBULK[-1::]


# In[19]:


jp.BEGINBULK[5:9]


# In[20]:


jp.BEGINBULK[5::9]


# In[21]:


jp.BEGINBULK[:]


# In[22]:


import matplotlib.pyplot as plt


# In[23]:


x = [1,2,3]


# In[24]:


y = [2,3,4]


# In[25]:


z = [3,5,6]


# In[26]:


plt.plot(x,y,z)


# In[27]:


plt.xlabel('x - axis')


# In[28]:


plt.ylabel('y - axis')


# In[30]:


plt.xlabel('x - axis')


# In[31]:


plt.ylabel('y - axis')


# In[32]:


plt.title('My first graph!')


# In[34]:


plt.show()


# In[35]:


plt.plot(x,y)


# In[14]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes()
plt.grid()
plt.show()


# In[ ]:




