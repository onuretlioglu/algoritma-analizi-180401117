#!/usr/bin/python3

import sys
import os
import random

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._dizi = [None]
    

    def _resize(self,capacity):                                         # private  resize metodu 
        tmp_dizi = capacity * [None]
        for i in range(self._n): 
            tmp_dizi[i] = self._dizi[i]                                 # yeni geçici dizine elemanlar copyalanır
        self._dizi = tmp_dizi
        self._capacity = capacity
    
    
    def append(self,obj):                                               # public append metodu 
        if self._n == self._capacity: self._resize(2*self._capacity)    # dizi kapasitesi katlanır 
        self._dizi[self._n] = obj                                       # obj diziye ekler 
        self._n += 1                                                    # dizi sayısını artırır. 
    
    
    def remove(self):                                                   # dizi boş değilse eleman silir 
        if self._n > 0:
            self._dizi[self._n] = None                                  # dizinin son elemen referans None olur
            self._n -= 1  



def main():                                                             #  main fonksiyonu
    dinamik_dizi = DynamicArray()
    
    dinamik_dizi.append(random.randint(0,10))
    dinamik_dizi.append(random.randint(0,10))
    dinamik_dizi.append(random.randint(0,10))
    dinamik_dizi.append(random.randint(0,10))
    dinamik_dizi.append(random.randint(0,10))
    
    print("Dinamic Dizi:")
    for i in dinamik_dizi: 
        print(i)
    
    dinamik_dizi.remove()
    dinamik_dizi.remove()
    
    print("Dizi son durumu:")
    for i in dinamik_dizi: 
        print(i)
        

if __name__ == "__main__":                                           #  main çağrımı
    main()
