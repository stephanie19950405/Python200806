# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:38:54 2020

@author: user
"""

import os.path

d={}
def bliudmenu():
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢')
    print('4.離開')
    a=input("請選擇一項服務")
    a=int(a)

print('#######################')
print('歡迎進入系統')
print('#######################')
  
      
if not os.path.isfile('scores.txt'):
    fo=open('scores.txt','w')
    print('new file')
else:
    fo=open('scores.txt','r')
    print('old file')

for row in fo.readlines():
    data=row.split(':')
    
    key=data[0]
    value=data[1]
    
    d[key]=value
print(d)

fo.close()

  
if bliudmenu()==1:  
        voc=0
        while voc==0:
            voc=input('請輸入名字')   
            g=input('請輸入成績')
            d[voc]=g
     
        r=int(input('按0退出,按1繼續')
        if r==0:
                x=x+1

    elif bliudmenu()==2:
         print(d)
         x=0

    elif bliudmenu()==3:
            x=0
            while x==0:
                voc=input('請輸入名字')
                for key,value in dict.items():
                    g=d[voc]
                    print[voc]
                  
                    else:
                        print('查無此資料')
                 
                    r=int(input('按0退出,按1繼續'))
                        if r==0:
                            x=x+1
    
    elif bliudmenu()==4:
        break
