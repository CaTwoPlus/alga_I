Goodland egy olyan ország, amelyben az összes város egy vonal mentén, egyenlő távolságra helyezkedik el egymástól. Az egymás melletti városok között 1 egységnyi távolság van. Az ország kormánya energia infrastruktúra fejlesztési projektet tervez, és meg szeretnék tudni, mi az a minimális erőmű szám, amely elegendő ahhoz, hogy az összes várost árammal lássák el. Ha nem lehetséges, hogy minden várost elérjen az áramellátás, akkor a válasz -1 legyen.

A feladatban adott egy városlista. Azon városok, ahol lehet erőművet építeni, 1-gyel vannak jelölve, a nem alkalmas városok pedig 0-val. 
Találd meg azt a minimális erőmű számot, amivel az összes város ellátható árammal, ha k = ellátási távolság. Azok a városok nem kapnak áramot, amelyeknél a távolság < k.

Példa
k = 3
arr = [0,1,1,1,0,0,0]
Vegyük az alábbi elrendezést, ahol minden város 1 egységnyi távolságra van a szomszédjától, és az indexelés 0-tól kezdődik. A következő városok alkalmasak erőmű építésére: 1, 2 és 3. Ha építünk egy erőművet az arr[2]-es városban, az képes ellátni az arr[0]-tól egészen az arr[4]-ig lévő városokat, mert ezek végpontok a hatótávolságon belül (2 egységen belül) vannak, tehát 2 < k. Az arr[6]-os város ellátásához szükség lenne egy erőműre a 4-es / 5-ös / 6-os városban, azonban ezek nem alkalmasak az erőmű építésére, így a válasz -1 lesz, mivel nem lehetséges minden várost ellátni árammal.

Függvény leírása

Implementáld a pylons függvényt, amely a következő paramétereket kapja:

- int k: az erőművek hatótávolsága
- int arr[n]: minden város alkalmassága az erőmű építésére (1= alkalmas, 0= nem alkalmas)

Visszatérési érték

int: a minimálisan szükséges erőművek száma, vagy -1, ha nem lehetséges minden várost ellátni.

Bemeneti formátum

Az első sorban két egész szám található: 
- 𝑛 a városok száma 
- 𝑘 az erőművek hatótávolsága

A második sorban 𝑛 darab, szóközzel elválaszott bináris szám található, ahol minden szám jelzi, hogy az adott város alkalmas-e erőmű építésére.

Korlátok
- 1 <= k <= n <= 10^5
- Minden arr[i] eleme {0,1} halmaznak

Részfeladat
- 1 <= k <= n <= 1000 igaz a maximum pont 40%-ára

Kimeneti formátum
- Az a legkisebb erűműszám, amivel elérhető, hogy minden városban legyen áram. 

Minta bemenet

STDIN         Function
-----         --------
6 2           arr[] size n = 6, k = 2
0 1 1 1 1 0   arr = [0, 1, 1, 1, 1, 0]


Minta kimenet

2

Magyarázat

Az c[1]-es, c[2]-es, c[3]-as és c[4]-es városok alkalmasak erőmű építésére. Minden erőmű hatótávolsága k = 2. Ha erőműveket építünk a c[1]-es és a c[4]-es városban, akkor az összes város el lesz látva árammal.