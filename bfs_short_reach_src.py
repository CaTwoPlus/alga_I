from collections import deque

# n = graf csucsainak szama, m = elek szama (nincs hasznalva), elek = elek listaja
# s = kezdo csucs
def bfs(n, m, elek, s):
    # 2d-s lista; minden csucsnak kulon listat hozunk letre, amely tartalmazza az adott csucshoz
    # kapcsolodo szomszedos csucsokat
    szomszedok = [[] for _ in range(n + 1)]
    # vegig megyunk az elek listajan, ahol minden u,v par egy elt jelol
    for u, v in elek:
        # v-t hozzaadjuk az u szomszedaihoz
        szomszedok[u].append(v)
        # u-t hozzaadjuk v szomszedaihoz, mert a graf iranyitatlan, az el ketiranyu
        szomszedok[v].append(u) 
    
    # kezdetben minden csucs elerhetetlen, tehat ertekuk = -1
    tavolsagok = [-1] * (n + 1)  
    # kezdőcsúcs távolsága 0, hiszen unmagatol 0-ra van
    tavolsagok[s] = 0  
    
    # BFS-hez letrehozunk egy deque-t, egy lista-szeru kontenert, amivel gyorsan
    # lehet elemeket hozzaadni, torolni a lista mindket vegerol. Belehelyezzuk a kezdocsucsot.
    sor = deque([s])
    
    # BFS algoritmus
    # addig fog futni, amig a sor ures nem lesz
    while sor:
        # kivesszuk a sor elejet, ami a jelenlegi csucs lesz
        jelenlegi = sor.popleft()
        
        # vegigmegyunk az csucs osszes szomszedjan
        for szomszed in szomszedok[jelenlegi]:
            # ha a szomszed csucsot meg nem latogattuk meg
            if tavolsagok[szomszed] == -1:
                # akkor a szomszed tavolsaga a jelenlegi csucs tavolsagahoz kepest 6-al lesz tobb
                tavolsagok[szomszed] = tavolsagok[jelenlegi] + 6
                # hozzaadjuk a szomszedot a sorhoz, hogy a sajat szomszedait is feldolgozhassuk
                sor.append(szomszed)
    
    # letrehozunk egy ures listat, amiben osszegyujtuk a kezdocsucstol valo tavolsagokat
    eredmeny = []
    # ha az aktualis index (i) nem a kezdocsucs (s), akkor a tavolsagat (tavolsagok[i]) hozzaadjuk
    # az eredmeny listahoz
    for i in range(1, n + 1):
        if i != s:
            eredmeny.append(tavolsagok[i])
    
    # visszaterunk a kezdocsucsbol a tobbi csucsba vezeto legrovidebb tavolsagokkal 
    return eredmeny

if __name__ == "__main__":
    t = int(input().strip())
    
    eredmenyek = []
    
    for _ in range(t):
        n, m = map(int, input().strip().split())
        
        elek = []
        for _ in range(m):
            u, v = map(int, input().strip().split())
            elek.append((u, v))
        
        s = int(input().strip())
        
        eredmeny = bfs(n, m, elek, s)
        eredmenyek.append(" ".join(map(str, eredmeny)))
    
    print("\n".join(eredmenyek))