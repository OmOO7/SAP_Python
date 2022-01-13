# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:33:31 2021

@author: 30048669
"""


a = """My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Zeel		My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Zeel		My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek"""


b = """My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek
My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek	My Name is Vivek"""


blen = b.count('\n')

LWithLines = []
LWithLines1 = []

LWithLines = b.split('\n')

LWithLines1 = a.split('\n')

#print(LWithLines)

print(len(LWithLines))


for i in LWithLines:
    print(i)
    print(len(i))
    programPause = input("Enter username:")
