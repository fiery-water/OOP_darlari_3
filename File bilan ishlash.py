# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:18:21 2023

@author: Mavlonbek
"""

import pickle

talaba1={'ism':'Mavlonbek','familya':'Toshtemirov','tyil':2004,'kurs':2}
talaba2={'ism':'Ibrohim','familya':'Parmonov','tyil':2004,'kurs':2}

faylnomi='new_file.txt'
ism='Mavlonbek Toshtemirov'
tyil=2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+"-da tug'ilgan"+'\n')
    
with open(faylnomi,'a') as fayl:
    fayl.write('Javlonbek Toshtemirov'+'\n')
    fayl.write("2007-da tuglgan"+'\n')
    
with open(faylnomi) as fayl:
    natija=fayl.read()
    
with open('students','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

with open('students','rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)
    
print(talaba1)
print(talaba2)
print(natija)