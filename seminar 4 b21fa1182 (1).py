#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x=np.arange(50,101)
print(x)


# In[2]:


import numpy as np
x=np.repeat(1,10)
y=np.repeat(0,10)
z=np.repeat(6,10)
np.concatenate([x,y,z])


# In[ ]:


import numpy as np
x=np.arange(20,32).reshape((3, 4))
print(x)


# In[ ]:


import numpy as np
x=np.eye(3,3)
print(x)


# In[ ]:


import numpy as np
x=np.diag([1,2,3,4,5])
print(x)


# In[ ]:


x=np.random.rand(2,3)
print(x)
a=np.sum(x)
b=np.sum(x, axis=0)
c=np.sum(x, axis=1)
print(a,b,c)


# In[ ]:


#salary

embid=[25467250,27504000,29542000,31579000,33616000]
curry=[45871000,48070000,51915000,557610000,59606000]
thompson=[32742000,35841000,37483210,40156743,43751264]
james=[35125168,38715231,41257000,43487610,45781354]
luka=[37514200,38451200,40164820,43152640,48214560]
morant=[8730415,9451256,9603415,12456125,14780520]
tatum=[28103500,30154876,32150345,34848350,37154786]
lillard=[39451230,41234125,43152100,45640123,48125412]
jokic=[34123510,35124120,37520150,40152341,43154201]
gobert=[35123410,36125410,38751012,40125630,44756120]

salary=np.array([ embid, curry, thompson, james, luka, morant, tatum, lillard, jokic, gobert])

print(salary.sum(axis=0))
print(salary.sum(axis=1))


# In[3]:


#Total games 

embid=[104,1, 84,124 ,34]
curry=[86,101 ,23,14 ,29]
thompson=[105,111 ,25 ,21 ,35]
james=[111 ,21 ,31,124,115]
luka=[112 ,13,114 ,15 ,16]
morant=[116,117 ,1, 56,80]
tatum=[105,110 ,12 ,19,121]
lillard=[112 ,21 ,13 ,15 ,17]
jokic=[101 ,3 ,5,7 ,10]
gobert=[105 ,10 ,12 ,19 ,21]

Totgame=np.array([ embid, curry, thompson, james, luka, morant, tatum, lillard, jokic, gobert])

print(Totgame.sum(axis=0))
print(Totgame.sum(axis=1))


# In[4]:


#total goals 

embid=[858,641, 645,124 ,741]
curry=[945,965 ,1015,1125 ,945]
thompson=[1015,865 ,895 ,945,845]
james=[851 ,945 ,1015,1124,1115]
luka=[1120 ,1321,1140,1510 ,1610]
morant=[1160,1170 ,1142, 1256,980]
tatum=[1050,1100 ,1210 ,1012,1210]
lillard=[1120 ,1221 ,1330 ,1512,1710]
jokic=[1010 ,1243 ,855,745 ,1010]
gobert=[1050 ,1012 ,2010 ,1429 ,2142]

Totgoals=np.array([ embid, curry, thompson, james, luka, morant, tatum, lillard, jokic, gobert])

print(Totgoals.sum(axis=0))
print(Totgoals.sum(axis=1))


# In[ ]:




