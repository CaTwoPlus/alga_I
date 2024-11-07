def pylons(k, arr):
    # n = varosok szama
    n = len(arr)
    eromuvek = 0
    # A jelenlegi varost indexeli
    i = 0       

    # Megvizsgaljuk az osszes varost
    while i < n:
        # Taroljuk a jelenlegi hatotavolsagon belul a legjobb helyet, ahova eromuvet epithetunk
        eromu_poz = -1
        # A hatotavolsagon belul hatrafele haladva keressuk az idealis varost
        for j in range(min(n - 1, i + k - 1), max(-1, i - k), -1):
            # Alkalmas varos eseten beallitjuk a poziciot, majd kilepunk a ciklusbol
            if arr[j] == 1:
                eromu_poz = j
                break
        
        # Ha nincs olyan varos a hatotavon belül, ahova eromuvet epithetnenk, visszaterunk -1-el
        if eromu_poz == -1:
            return -1
        
        # Hozzaadjuk az eromuvet es eloreugrunk a kovetkezo le nem fedett varosra
        eromuvek += 1
        i = eromu_poz + k

    return eromuvek

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    result = pylons(k, arr)

    print(result)