# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:10:00 2018

@author: Ritisha
"""
## Types of Variables ##

#Integer

x = 2 

print(type(x))

# Float 

y = 2.5

# String

a = "hello"

print(a)

print(type(a))

# Logical / Logical

q1 = True
print(type(q1))

#Use of variables
A = 10
B = 5

C = A + B

C

D = B / A

D

#Import module
import math

math.sqrt(A)

#Working with strings

greeting = "Hello"
name = "Bob"

message = greeting + " " + name

print(message)

#Boolean Variables and Operators

#2 values: True or False

4 < 5

# Operators
4 == 5 #equality

4 != 5 #inequality

# <, >, <=, >=, and, or, not

True and True

result =  not(4 > 5)

print(result)


 # 'while' loop
i = 0
 
while i < 2:
    print(i)
    i+=1
    
# 'for' loop
for i in range(5):
    print("Hello Python: ", i)    

print(list(range(5)))


mylist = [10, 100, 1000]
for i in mylist:
    print(i)     
 
# 'if' statement
    
import numpy as np
from numpy.random import randn

randn()

x = randn()

answer = None #None = NULL

if x > 1:
    answer = "greater than 1"
else:
    answer = "Less than 1"

print(x)
print(answer)

#Chained staatements
x = randn()

answer = None #None = NULL

if x > 1:
    answer = "greater than 1"
elif x >= -1:
    answer = "between -1 and 1"
else:
    answer = "less than -1"

print(x)
print(answer)

N = 100000
no = list(randn(N))

no

count = 0
for i in no:
    if i > -1 and i < 1:
        count += 1

print(count)
print(count / N)


