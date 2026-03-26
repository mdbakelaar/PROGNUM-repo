#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

class fib:
    def __init__(self, maxx, devide, final):
        self.maxx = maxx
        self.devide = devide
        self.final = final

    def array(self):
        seq = [0, 1]
        for i in range(2, self.final):
            seq.append(seq[i-1] + seq[i-2])
        return np.array(seq)

    def fib(self):
        fibnumb = self.array()
        
        mask = (fibnumb < self.maxx) & (fibnumb % self.devide == 0)
        fib_final = fibnumb[mask]
        return fib_final


f = fib(maxx = np.inf, devide=7, final=100)
results = f.fib()

print(f"The Fibonacci numbers smaller than {f.maxx} and divisible by {f.devide} are:")
print(results)


# In[ ]:




