#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd


# In[2]:


df = pd.read_excel (r'C:\Users\madhulika 1234\Desktop\baseball.xls')


# In[3]:


print(df)


# In[4]:


df.corr()


# In[5]:


df.cov()


# In[6]:


X = df[['YEAR','ATL','CHC']]


# In[7]:


Y = df[['WAS']]


# In[8]:


from numpy import array
from scipy.linalg import svd
print(X)
U, s, VT = svd(X)


# In[9]:


print(U)


# In[10]:


print(s)


# In[11]:


print(VT)


# In[13]:


from sklearn.preprocessing import StandardScaler
x_std = StandardScaler().fit_transform(X)


# In[14]:



x_std


# In[18]:


import numpy as np
# features are columns from x_std
features = x_std.T 
covariance_matrix = np.cov(features)
print(covariance_matrix)


# In[19]:


eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)


# In[20]:



print('Eigenvectors \n%s' %eig_vecs)


# In[21]:


print('\nEigenvalues \n%s' %eig_vals)


# In[22]:


eig_vals[0] / sum(eig_vals)


# In[23]:


projected_X = x_std.dot(eig_vecs.T[0])


# In[24]:


projected_X


# In[32]:


result = pd.DataFrame(projected_X, columns=['PC1'])
result['y-axis'] = 0.6
result['label'] = Y


# In[33]:


result.head()


# In[34]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[35]:


sns.lmplot('PC1', 'y-axis', data=result, fit_reg=False,  # x-axis, y-axis, data, no line
           scatter_kws={"s": 50}, # marker size
           hue="label") # color

# title
plt.title('PCA result')


# In[ ]:




