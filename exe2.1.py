##!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:58:26 2022

@author: jolien
"""
import numpy as np 
import pandas as pd 
########################### Exercise 2.1 #####################################
###1. Create two lists containing the names Peter, Claudia, Enrique, Matilde and
#the values social sciences, engineering, engineering, medicine

name = ["Peter", "Claudia", "Enrique", "Matilde"]
profession = ["social sciences", "engineering", "engineering", "medicine"]


###2. Create a dataframe called df2 from these two lists, the first variable being
#called firstNames, the second ageInYears 

df2 = pd.DataFrame(list(zip(name, profession)), columns = ["firstNames", "Profession"])
df2
###3. Add a column called age with the values values 21, 18, 20, 25
age = [21, 18, 20, 25]
df2["ageInYear"] = [21, 18, 20, 25]

df2 = pd.DataFrame(list(zip(name, profession, age)), columns = ["firstNames", "Profession", "ageInYear"])

###4.1 There is an error in the dataset. Matilde is 52! 
# the value without
#using iloc
df2["ageInYear"][3] = 52
df2

df2 = pd.DataFrame(list(zip(name, profession, age)), columns = ["firstNames", "Profession", "ageInYear"])

### 4.2 Enrique does not study engineering, but social sciences. Correct the error
#using the iloc method

df2.iloc[2,1] = "social sciences"#[row, column]mit 0 beginnen
df2
#df2 = pd.DataFrame(list(zip(name, profession, age)), columns = ["firstNames", "Profession", "ageInYear"])

###5. We want to join to df from above and df2, which we have just created above,
#with concatanate. But that does not work until we have renamed the variables
#of df2 to suit those of df. Use a method to show the names of each DF, then
#change the names of the variables of df2 to suit df and concatante them. Name 
#the new DF newDf

#df2.info()
df2.columns
#df2.index

a = ["Hans", "Lisa", "Ferdinand", "Rapuntzel"]
b =[21, 19, 25, 22]
df = pd.DataFrame(a, columns = ["names"])

df = pd.DataFrame(list(zip(a, b)), columns =["names", "age"])
df.index = ["a", "b", "c", "d"]
df["subject"] = ["social science", "medicine", "engineering", "social sciences"]
a = pd.Series(["Sigrid", 18, "medicine"], index=df.columns).rename("e")
df = df.append(a)


df.columns
#df.index
df
df.columns = ["names", "age", "subject"]

df2.columns =["names", "subject", "age"]

df2
newDf = df.append([df2])
newDf

#df zu list, columns tauschen und wieder zu df
#col_list = list(df2)
#col_list[1], col_list[2] = col_list[2], col_list[1]
#df2.columns = col_list

###6. Change the index so that the numbers 0 to 3 is converted to the letters 
#f to i


newDf.rename(index={0:"f", 1:"g", 2:"h", 3:"i"}, inplace=True)
newDf


###7. Ferdinand is actually called Fernando. Correct the value with loc.


newDf.loc[["c"], "names"] = "Fernando"

newDf


###8. Name the index "letters" and the columns the name "vars".


newDf.columns = ["vars1", "vars2", "vars3"]
newDf

newDf.index.name = "letters"
newDf


###9. Convert the letters index into a variable


varI = newDf.index
#varA = varA

#10. Move the letters variable to the end of the dataframe, convert the 
#variable name into the index.

newDf["end"] = varI
newDf

#index = varA
#newDf.reset_index()
#df.set_index("end")
newDf.set_index("varI", inplace = true)#testen ob richtig!!!!
newDf
#weiß nicht was er mit convert meint??

newDf.columns = ["name", "age", "profession", "index"]#nur name ändern oder zu index???




#11. Delete the variable letters
newDf.reset_index()
del newDf["letters"]
newDf.drop[columns=("letters")]
newDf
#funktioniert nicht

###12. Add the variable ageInDays, which takes the age (measured in years) and 
#multiplies it with 365

newDf.columns = ["name", "age", "profession", "index"]

Days = 365
ageInDays= Days * newDf.age
newDf["ageInDays"]= ageInDays
newDf

###13. We forgot Hans-Peter, who studies medicine and is 23 years old. Add him 
#to the dataframe (by creating a pd.Series).

j = pd.Series(["Hans-Peter", 23, "medicine", "j", Days*23], index = newDf.columns).rename("j")
newDf = newDf.append(j)
newDf
#newDf.drop("j")
########################### Excercise 2.1: End ################################