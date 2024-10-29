#!/bin/python3

import math
import os
import random
import re
import sys

# Min koltseg szamolasa, ahol k = baratok szama, c = viragok arait tartalmazo tomb
def getMinimumCost(k, c):
    # Csokkeno sorrendben valo rendezes segitsgevel minimalizalhato a teljes ar,
    # hiszen a dragabb viragokat veszik meg elobb az alacsonyabb szorzokkal
    c.sort(reverse=True)
    teljes_ar = 0
    vasarlasi_kor = 0
    
    # Nullatol indulva, a viragok db szamaig haladva, k = baratok szama = (vasarlasok szama / kor)-rel iteralva
    for i in range(0, len(c), k):
        # Megnezzuk, hogy a kovetkezo korre mennyi megvasarlasra varo virag marad, egysegesen szetosztva
        # a baratok kozott. Igy lehet elkerulni az c tomb tulindexeleset
        jelenlegi_kor = c[i:min(i + k, len(c))]
        
        # Virag ara = (vasarlasi_kor + 1) * virag ara
        for virag_ara in jelenlegi_kor:
            teljes_ar += (vasarlasi_kor + 1) * virag_ara
            
        vasarlasi_kor += 1
    
    return teljes_ar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()