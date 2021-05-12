# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:07:31 2021

@author: barto
"""
d = {'parzyste': [], 'nieparzyste': []}
for i in range(1,20):
    if i%2 == 0:
        d['parzyste'].append(i)
    if i%2 == 1:
        d['nieparzyste'].append(i)
print(d)


def funkcja(a,b):
    wynikdod = a + b
    wynikodej = a - b
    return (wynikdod, wynikodej)
b = funkcja(2,3)
print(b)
#print(b)