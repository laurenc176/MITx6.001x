# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:41:51 2020

@author: Lauren_C
"""
def genPrimes():
    """ A generator, genPrimes, that returns the sequence 
    of prime numbers on successive calls to its next() method"""
    
    primes = []
    x = 1
    while True:
        x += 1
        for p in primes:
            if x % p == 0:
                break
        else:
            yield x
            primes.append(x)
        
        