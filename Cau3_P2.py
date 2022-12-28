import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def ham_bac_4(a,b,c,d,e,x):
  y = x**4 - 2*x**2 - 3
  return y

x = np.linspace(start=-10.0,stop=10.0, num=200)
y = ham_bac_4(1,0, -2, 0,-3, x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
plt.show()

#đạo hàm của y
x = symbols('x')
y = x**4 - 2*x**2 - 3
y_phay = diff(y,x)
print(y_phay)

def ham_bac_3(a,b,c,d,x):
  y_phay = 4*x**3 - 4*x
  return y_phay

x = np.linspace(start=-10.0,stop=10.0, num=200)
y_phay = ham_bac_3(4,0,-4,0,x)
fig, ax = plt.subplots()
ax.plot(x, y_phay)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
plt.show()

#đạo hàm của y'
x = symbols('x')
y_phay = 4*x**3 - 4*x
y_phay_phay = diff(y_phay,x)
print(y_phay_phay)

def ham_bac_2(a,b,c,x):
  y_phay_phay = 12*x**2 - 4
  return y_phay_phay

x = np.linspace(start=-10.0,stop=10.0, num=200)

y_phay_phay = ham_bac_2(12,0,-4,x)
fig, ax = plt.subplots()
ax.plot(x, y_phay_phay)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
plt.show()

#đạo hàm của y''
x = symbols('x')
y_phay_phay = 12*x**2 - 4
y_phay_phay_phay = diff(y_phay_phay,x)
print(y_phay_phay_phay)

def ham_bac_1(a,b,x):
  y_phay_phay_phay = 24*x
  return y_phay_phay_phay

x = np.linspace(-10,10,200)

y_phay_phay_phay = ham_bac_1(24,0,x)
fig, ax = plt.subplots()
ax.plot(x, y_phay_phay_phay)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
plt.show()