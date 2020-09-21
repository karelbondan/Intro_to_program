# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:39:50 2020

@author: karel
"""

pi = 3.14
pie_diameter = eval(input("input pie diameter=", ))
pie_radius = pie_diameter // 2
circumference = (2*pi*pie_radius)
circumference_msg = "Jimmy's pie has a circumference:"
print(circumference_msg, circumference)