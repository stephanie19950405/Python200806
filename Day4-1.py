# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:04:31 2020

@author: user
"""

import os.path

if os.path.isfile('myfile.txt'):
    print('file存在')
else:
    print('file不存在')
    
fo=open('myfile.txt','w')
fo.write('You')

fo=open('myfile.txt','a')
fo.write(' and me')

fo=open('myfile.txt','r')
thefile=fo.read()
print(thefile)

fo.close()