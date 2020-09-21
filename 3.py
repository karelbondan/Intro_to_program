# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:19:56 2020

@author: karel
"""

cls1,cls2,cls3 = eval(input("Input the number of students in class 1, 2, and 3 sequentially, separated by commas= ", ))

a,b,c = (cls1//5), (cls2//7), (cls3//6)
x,y,z = (cls1%5),(cls2%7),(cls3%6)
print("Number of students in each group:")
print("Class 1:", a)
print("Class 2:", b)
print("Class 3:", c)

print("Number of students leftover:")
print("Class 1:", x)
print("Class 2:", y)
print("Class 3:", z)
