#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from math import log, ceil

def bisection(f, a, b, tol):


  if (a > b):
    print("a < b is not true. Correct a and b!\n")
    return

  if f(a) == 0: return a
  if f(b) == 0: return b  

  if ((np.sign(f(a)) * np.sign(f(b))) > 0):
    print("Root is not bracketed. Correct a and b!\n")
    return

  n = ceil(log(abs(b-a)/tol)/log(2.0))
  
  print("--------------------------------------------------------------------------")
  print(" n \t     a \t         b \t     c \t       b-c \t f(c)        ")
  print("--------------------------------------------------------------------------")

  for i in range(n):

    c = (a+b)/2

    print(" %.0f  %.8f  %.8f  %.8f  %.8f %.8f" %((i+1), a, b, c, (b-c), f(c)))

    if ((b-c) <= tol):
      print("--------------------------------------------------------------------------")
      print("Root found: %.8f" %c)
      return

    if ((np.sign(f(b)) * np.sign(f(c))) <= 0):
      a = c
    else:
      b = c


# In[ ]:


def newton(f, df, x0, epsilon, max_iter):


  if abs(f(x0)) < epsilon:
    print("Root found: %.8f" %x0)
    return

  fx0 = f(x0)
  dfx0 = df(x0)

  if dfx0 == 0:
    print("The derivative is zero at %.8f! STOP!" %x0)
    return None

  x1 = x0 - fx0/dfx0

  print("--------------------------------------------------------------------------")
  print(" n \t   x_n \t      f(x_n)\t  x_n-x_n-1")
  print("--------------------------------------------------------------------------")
  print(" 0  %.8f  %.10f             -- \t" %(x0, fx0))
  
  for k in range(1,max_iter+1):

    fx = f(x1)
    dfx = df(x1)
    
    if dfx == 0:
      print("The derivative is zero at %.8f! STOP!" %x1)
      return None
    
    error = x1 - x0
    print(" %.0f  %.8f  %.10f  %.10f" %(k, x1, fx, error))
        
    if (abs(fx) < epsilon) & (abs(error) < epsilon):
      print("--------------------------------------------------------------------------")
      print("Root found: %.8f" %x1)
      return
    
    x0 = x1
    x1 = x1 - fx/dfx
  
  print("Exceeded maximum iterations!")
  return None


# In[ ]:


def secant(f, x0, x1, err_bd, max_it):


  fx0 = f(x0)
  fx1 = f(x1)
  error = 1
  i = 0

  print("--------------------------------------------------------------------------")
  print(" n \t   x_n \t      f(x_n)\t   x_n-x_n-1\t")
  print("--------------------------------------------------------------------------")
  print(" %.0f  %.8f  %.10f             -- \t" %(i, x0, fx0))

  i = 1
  print(" %.0f  %.8f  %.10f    %.10f" %(i, x1, fx1, (x1-x0)))

  while (abs(fx1) > err_bd) & (abs(error) > err_bd):

    i = i+1

    if (fx1 == fx0):
      print("f(x1) = f(x0); Division by zero! STOP!")
      return None

    x2 = x1 - (x1-x0)*fx1/(fx1-fx0)

    x0 = x1
    x1 = x2
    fx0 = fx1
    fx1 = f(x2)
    error = x1 - x0

    print(" %.0f  %.8f  %.10f    %.10f" %(i, x1, fx1, error))
    
    if (i > max_it):
      print("Exceeded maximum iterations!")
      return None

  print("--------------------------------------------------------------------------")
  print("Root found: %.8f" %x2)


# In[ ]:




