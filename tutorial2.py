# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:49:37 2018

@author: Ritisha
"""
#Create Lists
MyFirstList = [3,45, 56, 732]
type(MyFirstList)

l2 = ["Hello", 24, True, 55.3]
type(l2)

l3 = ['how are you', 55, MyFirstList]

#Function 'range'

range(15) #In python 3, range is iterator

#Only one argument means it starts at 0
list(range(15))

list(range(1,8))

list(range(100,111, 2)) #3rd argument is the step

#Accessing elements in list
w = ['a', 'b', 'c', 'd', 'e']

w[0]

#Length of list
len(w)

#Negative indexation
w[-1] #Gives last element of the list

#Overwrite values
w[2] = 63
w


#Slicing lists
l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
l1[:] #Full List

l1[2:] #From element 2 to the end

l1[2:7] #From 2 to 6 (7 is not inclusive)

l1[-8:7] #Negative indexation can also be used

l1[2:9:2] #Advanced Slicing, 3rd argument is step

l1[::3]

l1[7:2:-1]

#Tuples

t1 = (345, 674, 934)

t1[0]


#Functions in Python

range(20,31)

mylist1 = list(range(20,31))

print(mylist1)

len(mylist1)

type(mylist1)

max(mylist1)

min(mylist1) # Can be passed a series of values




#Install packages

import scrapy


from scrapy.crawler import CrawlerProcess

#Arrays 
l = [23245, 27, 546,215, -1234]

import numpy as np

a = np.array(l) #converts a List to Array

type(a)

a.mean()

a[2:]

b = a[2:4] #Here, b is just another view for array a

b[:] = 111 #This will impact our original array a

a

c = a.copy() #Create a copy of a i.e. allocate separate memory for c





