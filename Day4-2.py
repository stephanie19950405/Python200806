# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:59:02 2020

@author: user
"""

file=open('楓葉.jfif','rb')
img=file.read()
file.close()

file=open('copy.jpg','wb')
file.write(img)
file.close()