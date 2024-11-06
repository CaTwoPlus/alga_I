Legrövidebb út szélességi kereséssel

Gondoljunk egy irányítatlan gráfra, ahol minden él 6 egységnyi súlyú. Minden csúcsot sorban 1-től n-ig címkézünk.

Egy sor lekérdezést kapunk. Minden lekérdezéshez kapunk egy él-listát, amely egy irányítatlan gráfot ír le. Miután elkészítettük a gráf reprezentációját, meg kell határoznunk a legrövidebb távolságot az összes többi csúcshoz egy adott kiindulási helyzetből a szélességi keresés (BFS) algoritmus segítségével. Egy távolságtömböt kell visszaadni a kezdőcsúcsból kiindulva, csúcsszám szerint növekvő sorrendben. Ha egy csúcs nem elérhető, akkor azt a csúcsot jelölje -1.

Példa
A következő gráf az alábbi bemenetek alapján jött létre:

(kép4)

n = 5 // csúcsok száma
m = 3 // élek száma
élek = [1,2],[1,3],[3,4]
s = 1 // kezdőcsúcs

Minden távolság a kezdőcsúcsból indul. A kimenet a távolságokat adja vissza a csúcsokhoz 5:[6,6,12,-1]-től 2-ig. Minden él 6 egységnyi, és a nem elérhető 5-ös csúcsnak van egy kötelező -1-es visszatérési értéke.

Függvény leírása

Egészítsd ki a bfs függvényt az alábbi szerkesztőben. Ha egy csúcs nem elérhető, annak távolsága -1.

A bfs függvénynek a következő paraméterei vannak:

int n: a csúcsok száma
int m: az élek száma
int élek[m][2]: élek kezdő és végpontjai
int s: a kiindulási csúcs

Visszatérés

int[n-1]: a távolságok csúcsszám szerint növekvő sorrendben, a kezdőcsúcs nélkül (-1, ha egy csúcs nem elérhető)

Bemenet formátuma

Az első sor egy egész számot tartalmaz, q-t, a lekérdezések számát. A következő sorok mindegyike a következő formátumban van:

Az első sor két szóközzel elválasztott egész számot tartalmaz, n-et és m-et, a gráf csúcsainak és éleinek száma.
Az ezt követő sor mindegyike két szóközzel elválasztott egész számot tartalmaz, u-t és v-t, amelyek egy élt írnak le u és v csúcsok között.
Az utolsó sor egyetlen egész számot tartalmaz, s-et, azaz kezdőcsúcs számát.

Korlátozások

1 <= q <= 10
2 <= n <= 1000
1 <= m <= (n*(n-1))/2
1 <= u,v,s <= n

Mintabemenet

2
4 2
1 2
1 3
1
3 1
2 3
2

Mintakimenet

6 6 -1
-1 6

Magyarázat

A következő két lekérdezést hajtjuk végre:

1.) A megadott gráf így reprezentálható:

(kép5)

ahol a kezdő s csúcsunkra igaz, hogy s = 1. A legrövidebb távolságok s-től a többi csúcsig:
- él a 2-es csúcsig
- él a 3-as csúcsig
- végtelen távolság a 4-es csúcsig (amelyhez nem kapcsolódik). 

Végül egy távolságtömböt adunk vissza az 1-es csúcsból a 2-es, 3-as, és 4-es csúcsokhoz (sorrendben): [6,6,-1].

2.) A megadott gráf így reprezentálható:

(kép6)

ahol a kezdőcsúcsunk, s, a 2-es csúcs. Itt csak egy él van, így az 1-es csúcs nem elérhető a 2-es csúcsból, és a 3-as csúcsnak egy éle van, amely összeköti a 2-es csúccsal. Végül egy távolságtömböt adunk vissza a 2-es csúcsból az 1-es és 3-as csúcsig (sorrendben): [-1,6].

Megjegyzés: Emlékezzünk, hogy minden él hossza 6, és -1-et adunk vissza bármely olyan csúcs távolságaként, amely nem érhető el s-ből.