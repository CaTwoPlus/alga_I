Red John visszatért

Red John újabb gyilkosságot követett el. Ezúttal nem hagy vörös mosolyt maga után. Ehelyett egy rejtvényt hagyott Patrick Jane-nek. SMS-t is küldött Teresa Lisbonsnak, hogy ha Patrick sikeres, feladja magát. A rejtvény így kezdődik.

Az áldozat házában van egy 4xn méretű fal. Az áldozatnak végtelen mennyiségű 4x1 és 1x4 méretű téglája van a házában. Van egy rejtett széf, amely csak egy adott téglakonfigurációval nyitható ki. Először ki kell számítani az összes lehetséges módot, ahogyan a téglákat el lehet rendezni úgy, hogy az egész falat lefedjék. Az alábbi diagram bemutatja, hogyan lehet téglákat elrendezni, hogy lefedjék a falat, ahol :

1 <= n <= 4

(kép1)

Van még egy lépés a rejtvényben. Jelöljük a lehetséges elrendezések számát M-el. Patricknek meg kell határoznia az inklúzív 0 - M tartományba eső prímszámok P számát.

Példaként vegyük az n = 3 esetet. A fenti diagram alapján meghatározzuk, hogy csak egy olyan elrendezés van, amely helyesen lefedi a falat. Az 1 nem prímszám, így P = 0.

Egy összetettebb példa az n = 5 eset. A téglák összesen 3 konfigurációban helyezhetők el úgy, hogy a falat lefedjék. A 2 és a 3 prímszámok, 2,3 <= 3, tehát P = 2. 

(kép2)

Függvény leírása

A redJohn függvény paraméterei:

- n: egy egész szám, amely a fal hosszát jelzi

Bemenet formátuma

Az első sor tartalmazza a t egész számot, azaz a tesztesetek számát.
A következő t sorok mindegyike tartalmaz egy egész n számot , amely a fal 4 x n hosszát jelzi.

Korlátozások

1 <= t <= 20
1 <= n <= 40

Kimenet formátuma

Külön sorokba nyomtasd ki az egyes tesztesetek P értékét.

Mintabemenet

2  
1  
7  

Mintakimenet

0  
3  

Magyarázat

Ha n = 1, a téglákat csak egyféleképpen lehet lerakni: függőlegesen.

Az értékhez tartozó prímszámok száma <= 1, azaz 0.

Ha n = 7, az egyik mód, ahogyan a téglákat lerakhatjuk, a következő:

(kép3)

Ebben az esetben 5 a lehetséges tégla elrendezési szám , és 3 prímszám található, ami <= 5.