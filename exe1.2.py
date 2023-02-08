#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:15:45 2022

@author: jolien
"""

############################ Exercise 1.2 ####################################
#1. Describe, in your own words, the difference between mutable and immutable
#data types.

#mutable data: alte werte einer variablen werden mit einer neuen variablen mit neuen werte überschrieben
#immutible data: sind unveränderliche ob jekte

#2. Consider the following code:
a = 12345
b = a
c = 12345
#Try to predict the expected output of each line below and check whether 
#you were right 
a == b #true
a is b#true
a == c#true
a is c#false weil c auf anderer position in speicher, andere id
#Now explain the output of the following lines of code (somewhat comprehensively) 

#3. Compare the functions and methods that were applied to lists and tuples.
#What can be done with lists that cannot be done with tuples?
#lists werte sind veränderbar durch verschiedene funktionen