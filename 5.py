# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:40:05 2020

@author: karel
"""

speed = eval(input("enter speed (in meter)= "))
freq = eval(input("enter frequency (in Hz)= "))
x = speed/freq
print("The speed (m/s):", speed)
print("The frequency (Hz):", freq)
print("The wavelenght (m):", x)