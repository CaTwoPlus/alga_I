Mohó virágárus

Egy baráti társaság szeretne egy csokor virágot vásárolni. A virágárus szeretné maximalizálni új vásárlóinak számát, illetve a bevételét. Ehhez úgy dönt, hogy minden virág árát megszorozza az adott vásárló által korábban vásárolt virágok számával, majd hozzáad egyet. Az első virág eredeti áron lesz, (0 + 1) * eredeti ár, a következő (1 + 1) * eredeti ár, és így tovább.

Adott a baráti társaság létszáma, a vásárolni kívánt virágok száma és a virágok eredeti ára. Határozd meg a minimum költséget az összes virág megvásárlásához. A kívánt virágok száma megegyezik a c tömb hosszával.

Példa
c = [1,2,3,4]
k = 3

A  tömb hossza c = 4, így összesen 4 virágot szeretnének vásárolni. Mindegyikük eredeti áron vásárolja meg a [2,3,4] árú virágok közül az egyik virágot. Miután mindannyian vásároltak x = 1 virágot, a lista első virága c[0], ára (jelenlegi vásárlás  +  korábbi vásárlás) * c[0]  =  (1 + 1)*1  =  2 lesz. Az összköltség tehát 2 + 3 + 4 + 2  =  11.

Függvény leírása
A getMinimumCost függvény a következő paraméterekkel rendelkezik:
-int c[n]: minden virág eredeti ára
-int k: a barátok száma

Visszatérési érték
-int: a minimális költség az összes virág megvásárlásához

Bemenet formátuma
Az első sor két szóközzel elválasztott egész számot tartalmaz: n és k, azaz virágok és a barátok számát.
A második sor n darab, szóközzel elválasztott pozitív egész számot tartalmaz: c[i], azatz minden virág eredeti árát.

Megkötések
1 <= n, k <= 100
1 <= c[i] <= 10^6
válasz < 2^31
0 <= i < n

Minta bemenet 0
3 3  
2 5 6  

Minta kimenet 0
13  

Magyarázat 0
Van n = 3 virág c = [2,5,6] költségekkel és k = 3 fővel a csoportban. Ha mindenki vesz egy virágot, az árak összesen 2 + 5 + 6 = 13 dollárra rúgnak. Így a válasz 13 lesz.

Minta bemenet 1
3 2  
2 5 6  

Minta kimenet 1
15  

Magyarázat 1
Van  n = 3 virág c = [2,5,6] költségekkel és k = 2 fővel a csoportban. Minimalizálhatjuk az összköltséget a következőképpen:

1.) Az első személy csökkenő ár sorrendjében 2 virágot vásárol; először a drágább virágot (c1 = 5) veszi meg p1 = (0 + 1) * 5 = 5 dollárért, majd a következő, olcsóbb virágot p0 = (1 + 1) * 2 = 4 dollárért.

2.) A második személy a legdrágább virágot veszi meg p2 = (0 + 1) * 6 = 6 dollárért.

A vásárlások összegét, azaz 5 + 4 + 6 = 15 nyomtatjuk válaszként.

Minta bemenet 2
5 3  
1 3 5 7 9  

Minta kimenet 2
29  

Magyarázat 2
A barátok megvásárolják a virágokat 9, 7 és 3, 5 és 1 áron 9 + 7 + 3 * (1 + 1) + 5 + 1 * (1 + 1) = 29 összköltségért. 
