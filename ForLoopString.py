# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:33:44 2021

@author: 30048669
"""

import sys


# a = """My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Zeel		My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Zeel		My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek"""


# b = """My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
# My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek"""
a = """51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 5.76 	 141.44 
						 -   
						 -   
						 -   
 51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 5.76 	 141.44 
 51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 0.07 	 135.74 
						 -   
					 5.69 	 5.69 
 51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 5.76 	 141.44 """


b = """51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 5.76 	 141.44 
						 -   
						 -   
						 -   
 51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 5.76 	 141.44 
 51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 0.07 	 135.74 
						 -   
					 5.69 	 5.69 
 51.42 	 80.33 	 3.87 	 0.00 	 0.06 	 5.76 	 141.44 """

print(a==b)
al= []
bl= []

al = a.split()
bl = b.split()

print(al)
print(bl)

l= len(a)

blen = b.count('\n')

#sys.exit()
cnt = 0
for i in range(l):
    #print(i)
    index1 = a[i]
    index2 = b[i]
    cnt = cnt + 1
    if index1 == index2:
        pass
    else:
        str1 = b[i:l]
        #print(str1)
        break
        
print(str1)    
str1 = str1.split()[0]
print(str1)
print(cnt)
