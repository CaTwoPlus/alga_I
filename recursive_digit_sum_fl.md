Számjegyek összege rekurzívan

Egy egész szám, x, szuper számjegyét a következő szabályok alapján definiáljuk:

Adott egy egész szám, amelynek meg kell határoznunk a szuper számjegyét.

Ha x csak 1 számjegyből áll, akkor annak szuper számjegye maga az x. Ellenkező esetben x szuper számjegye megegyezik x számjegyei összegének szuper számjegyével. Például 9875 szuper számjegye így lesz kiszámítva:

super_digit(9875)   	9+8+7+5 = 29 
super_digit(29) 	2 + 9 = 11
super_digit(11)		1 + 1 = 2
super_digit(2)		= 2  

Példa
n = ' 9875'
k = 4

A p számot az n string k-szoros összefűzésével hozzuk létre, így kezdetben p = 9875987598759875.

superDigit(p) = superDigit(9875987598759875)
              9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
superDigit(p) = superDigit(116)
              1+1+6 = 8
superDigit(p) = superDigit(8)

A p számjegyeinek összege 116. A 116 számjegyeinek összege 8. A 8 csak egy számjegy, tehát ez lesz a szuper számjegy.

Függvény leírása
A superDigit a következő paraméterekkel rendelkezik:

string n: egy egész szám string formában
int k: hányszor kell n-et összefűzni, hogy p-t kapjunk

Visszatérítési érték
int: a k-szor ismételt szuper számjegye n-nek

Bemenet formátuma
Az első sorban két szóközzel elválasztott egész szám található, n és k.

Megkötések
1 <= n <= 10^100000
1 <= k <= 10^5 

Minta bemenet 0
148 3 

Minta kimenet 0
3 

Magyarázat 0
Itt n = 148 és k = 3, így p = 148148148.

super_digit(P) = super_digit(148148148)
            = super_digit(1+4+8+1+4+8+1+4+8)
            = super_digit(39)
            = super_digit(3+9)
            = super_digit(12)
            = super_digit(1+2)
            = super_digit(3)
            = 3

Minta bemenet 1
9875 4 

Minta kimenet 1
8 

Minta bemenet 2
123 3 

Minta kimenet 2
9 

Magyarázat 2
Itt n = 123 és k = 3, így p = 123123123.

super_digit(P) = super_digit(123123123)
            = super_digit(1+2+3+1+2+3+1+2+3)
            = super_digit(18)
            = super_digit(1+8)
            = super_digit(9)
            = 9