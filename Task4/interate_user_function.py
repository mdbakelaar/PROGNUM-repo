#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy.integrate import quad
from numpy import sin, cos, exp, pi

# letting you enter a function
userfunc = input("Enter function in terms of x (e.g., x**4 + exp(sin(x) + cos(x))): ")

# evaluate what the user uses as a function
def f(x):
    return eval(userfunc, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi})

try:
    # using quad function to integrate
    area = quad(f, 0, pi)
    print(f"Integral from 0 to pi using quad gives: {area}")

    # Monte Carlo parameters
    N = 100000
    a = 0
    b = pi

    # random numbers
    g = np.random.uniform(a, b, N)
    fx = f(g) 

    # Monte Carlo integration
    mcintegral = (b - a)/len(g) * np.sum(fx)

    print(f"Integral from 0 to pi using Monte Carlo gives: {mcintegral}")
    
#If the user inputs a wrong function and would normally get an error there are now except functions to tell the user what they did wrong
except NameError as e:
    print("Error: Unknown function or variable used.")
    print(e)

except SyntaxError:
    print("Error: Invalid mathematical expression.")

except Exception as e:
    print("Something went wrong:")
    print(e)


# In[ ]:




