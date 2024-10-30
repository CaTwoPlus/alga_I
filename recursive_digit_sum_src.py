# n = input szam, k = hanyszor kell osszefuzni n-et 
def superDigit(n, k):
    # Ha szamjegy hossza 1, akkor a szuper szamjegye = 1
    if len(n) == 1:
        return int(n)
    else:
        # n minden substringjet integerre alakitva megszamoljuk a szamjegyek osszeget
        szamj_osszege = sum(int(d) for d in n) * k
        # visszaalakitjuk n-et stringge, majd rekurzivan meghivjuk a fgv-t a szamjegyek uj osszegevel
        # mivel k-val mar beszoroztunk elobb, k erteke 1 lesz
        return superDigit(str(szamj_osszege), 1)
    
if __name__ == "__main__":
    n, k = input().split()
    n = str(n)
    k = int(k)
    print(superDigit(n, k))