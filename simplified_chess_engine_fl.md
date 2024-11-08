A sakk egy nagyon népszerű játék, amelyet emberek százmilliói játszanak. Manapság léteznek sakkprogramok, mint például a Stockfish és a Komodo, amelyek segítenek a partik elemzésében. Ezek a programok rendkívül fejlett szoftverek, amelyek intelligens ötleteket és algoritmusokat alkalmaznak a pozíciók és lépéssorozatok elemzésére, illetve taktikai megoldások felfedezésére. Tekintsünk most egy egyszerűsített sakkváltozatot:

Tábla: Két játékos játszik rajta, 4 x 4-es táblán, akiket Fekete és Fehér néven nevezünk.

Figurák és Mozgás:

- Fehér kezdetben w darab figurával rendelkezik, míg Feketének b darab figurája van.
- A táblán nincsenek királyok és gyalogok. Mindkét játékosnak pontosan egy királynője van, legfeljebb két bástyája, valamint legfeljebb két könnyű tisztje (azaz egy futó és/vagy egy huszár).
- Minden figura ugyanazokat a lépéseket teheti meg, mint a hagyományos sakkban, és minden lépés egyetlen lépésnek számít, bármelyik játékos esetén.
- A klasszikus sakktól eltérően nincs döntetlen, ha a pozíciók ismétlődnek.

Cél: A játék célja, hogy elfogjuk az ellenfél királynőjét anélkül, hogy elveszítenénk a sajátunkat.

Adott m, a maximális lépésszám, illetve g számú játék esetén a figurák elhelyezkedése. Implementáljunk egy nagyon egyszerű (az igazi sakkprogramokhoz képest) motort az egyszerűsített sakkváltozatunkhoz, amely képes meghatározni, hogy Fehér győzhet-e <= m lépésben (függetlenül attól, hogyan játszik Fekete), feltéve, hogy minding Fehér kezd. Minden játékra nyomtassuk ki egy új sorban, hogy Fehér győzhet-e a megadott feltételek mellett. Ha lehetséges, írjuk ki, hogy IGEN; ellenkező esetben NEM.

Bemeneti formátum
Az első sor egyetlen egész számot tartalmaz, g-t, amely az egyszerűsített sakkjátszmák számát jelöli.
Az ezt követő sorok az egyes játékokat a következő formátumban határozzák meg:

- Az első sor három szóközzel elválasztott egész számot tartalmaz: w (Fehér figurák száma), b (Fekete figurák száma) és m (a maximális lépésszáma Fehér esetleges győzelmének).
- A következő w + b sor mindegyikében egy sakkfigura szerepel t c r formátumban, ahol a t egy karakter, és eleme a {Q,N,B,R} halmaznak, amely a figura típusát jelöli (ahol Q a királynőt, N a huszárt, B a futót és R a bástyát jelenti), c és r pedig a tábla azon oszlopát és sorát jelöli, ahova a figura kerül (ahol c eleme {A,B,C,D} halmaznak és r eleme {1,2,3,4} halmaznak).
- A következő w sor mindegyike egy fehér figura típusát és helyzetét jelöli a táblán.
- A következő b sor mindegyike egy fekete figura típusát és helyzetét jelöli a táblán.

Megkötések
- Biztosított, hogy az összes megadott figura helyzete különböző.
- 1 <= g <= 200
- 1 <= w,b <= 5
- 1 <= m <= 6

Minden játékos kezdetben pontosan egy királynővel, legfeljebb két bástyával és legfeljebb két könnyű tiszttel rendelkezik.

Kimeneti formátum
Az egyes g egyszerűsített sakkjátszmákhoz nyomtassuk ki új sorban, hogy Fehér győzhet-e <= m lépésben. Ha lehetséges, írjuk ki, hogy IGEN; ellenkező esetben NEM.

Példa bemenet 0

1
2 1 1 
N B 2
Q B 1
Q A 4

Példa kimenet 0

IGEN

Magyarázat 0

Az egyszerűsített g = 1 sakkjátékban a figurák kezdeti elhelyezkedése a következő:

(kép7)

Fehér következik, és egyetlen lépésben megnyerheti a játékot azzal, hogy a huszárját az A4 mezőre helyezi, és elfogja Fekete királynőjét. Mivel egy lépés alatt sikerült győzni, és 1 <= m, ezért IGEN-t nyomtatunk egy új sorban.