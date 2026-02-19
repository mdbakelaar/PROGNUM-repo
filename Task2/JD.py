#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math

Years = Y = input("Enter current year: ")
Months = M =  input("Enter current month (1-12): ")
Days = D =  input("Enter current day: ")

Y = int(Years)
M = int(Months)
D = int(Days)

JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5

Years2 = Y2 = input("Enter any year: ")
Months2 = M2 =  input("Enter any month (1-12): ")
Days2 = D2 =  input("Enter any day: ")

Y2 = int(Years2)
M2 = int(Months2)
D2 = int(Days2)

JD2 = 367*Y2 -7*(Y2+(M2+9)/12)/4 - 3*((Y2+(M2-9)/7)/100 + 1)/4 + (275*M2)/9 + D2 + 1721029-0.5

B = abs(JD2-JD)

jd = f"The amount of days between your chosen dates: {B}"
print(jd)


# In[ ]:




