#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:03:08 2022

@author: jolien
"""

import numpy as np 
import pandas as pd 
import random

mtcars = pd.read_csv("/Users/jolien/Desktop/Python/mtcars.csv")

############################# Exercise 5.1 ####################################
#1.Sort mtcars by carNames, am and gear (in that order). Reset the index. 
#Save it as mtcars2.

mtcars11 = mtcars.sort_values(["carNames", "am", "gear"]) 
mtcars11
mtcars2 = mtcars11.reset_index() 

mtcars2.head()
mtcars2[2:3]

#2.Filter all out cars that an mpg bigger than 25

mtcars[mtcars["mpg"]>25]

#3.Filter all cars that have an mpg smaller or equal to 25 and hp value bigger
#than 75
mtcars[(mtcars["mpg"] <= 25) & (mtcars["hp"]>75)]



#4.Filter all cars that have 4 gears and an am value of 0
mtcars.columns
mtcars[(mtcars["gear"] == 4) & (mtcars["am"]==0)]

#5.Filter all cars that have 4 gears or an am value of 0

mtcars[(mtcars["gear"] == 4) | (mtcars["am"]==0)]

#6.Explain the difference between the results of ex. number 3 and 4 in your own
#words

#??? vielleicht meint er eher 4 und 5
# bei 4 müssen beide bedingungen erfüllt sein für true
#bei 5 muss nur die erste oder (!) die zweite bedingung erfüllt sein

#7.What do boolean values have to do with this line of code? Demonstrate

False and True # = False

True | False # = True

#8.Filter all cars that have a cyl value of 4 or greater and a vs value of 0
#or an am value of 1

mtcars[(mtcars["cyl"] >= 4) & (mtcars["vs"]==0) | (mtcars["am"] ==1)]

########################### Exercise 5.1: End #################################
