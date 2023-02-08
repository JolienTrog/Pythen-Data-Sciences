#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 11:17:08 2022

@author: jolien
"""

#1. Create a list with the values from 0 to 99 with range. Call it list1

list1 = [i for i in range(0, 100)]

#2. Select the range of numbers from 10 to 20 and create a new list called list2
list2 = list1[9:20]

#3. Create a new list called superList, which consists of both list1 and list2.

superList = [list1, list2]
print(superList)

#4. Delete the number 99 in list1 in superList.

superList[0][98]
del superList[0][99]
print(superList)

superList[0].remove(99)

#5. Add a new list to superlist called list3 which contains the letters a, b, c, d.

list3 = [["a", "b", "c", "d"]]
superList.extend(list3)


#6. Add the values a, b, c, d directly to superList.
print(superList + list3)


#7. Create a new list containing the values of list1 in superList from the number
#11 to the last number in list1. Call it newList, which exists independently of
#superList

newList = superList[0][10:]#wenn man zahl 11 will dann mit 10 anfangen da index bei 0 anfängt


#8. Reverse the order of the values contained in newList.

newList.reverse()

#9. Duplicate the series of values in newList

newList*=2

dir(newList)

#10. Sort the values from small to big

newList.sort()

#11. Create a list called newList2 from list2 in superList, which contains only
#every second value, starting with the first

newList2 = superList[1][0:11:2]

#11. Find the min and max values in randomList (using functions) and calculate 
#the range, naming that value r1. To generate randomList, uncomment (i.e.
#delete # symbols) of the two lines of code below and execute


import random 
randomList = random.sample(newList, 10)
min(randomList)
max(randomList)
r1 = max(randomList) - min(randomList)

#12. Create a tuple containing the values a, b, c, d. Call it tuple1

tuble1 = ("a", "b", "c", "d")

#13. Add the letter "e" to the tuple 

tuble1 += ("e",)

#14. Get rid of the letter "c" in tuple1

tubList = list(tuble1)
del tuble1[2]
tubNoC = tuble(tubList)
print(tuble1)
