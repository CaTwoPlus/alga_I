from bfs_short_reach_src import bfs

def run_teszt_esetek():
    # Tesztesetek (n, m, elek, s, várt_eredmény)
    teszt_esetek = [
        (4, 2, [(1, 2), (1, 3)], 1, [6, 6, -1]), 
        (3, 1, [(2, 3)], 2, [-1, 6]), 
        (5, 4, [(1, 2), (1, 3), (3, 4), (4, 5)], 1, [6, 6, 12, 18]), 
        (6, 5, [(1, 2), (1, 3), (3, 4), (4, 5), (5, 6)], 3, [6, 12, 6, 12, 18]),  
        (7, 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)], 4, [18, 12, 6, 6, 12, 18]), 
        (8, 7, [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 4, [12, 6, 18, 24, 6, 30, 12]),  
        (9, 9, [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9)], 1, [6, 6, 12, 12, 18, 18, 24, 24]),  
        (10, 12, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)], 5, [24, 18, 12, 6, 6, 12, 18, 24, 30]),  # OK - nem változott
        (15, 14, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15)], 8, [42, 36, 30, 24, 18, 12, 6, 6, 12, 18, 24, 30, 36, 42]),  
        (20, 19, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20)], 10, [54, 48, 42, 36, 30, 24, 18, 12, 6, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60])  
    ]
    
    for i, teszt in enumerate(teszt_esetek, 1):
        n, m, elek, s, vart_eredmeny = teszt
        eredmeny = bfs(n, m, elek, s)
        
        print(f"\nTeszt #{i} eredmények:")
        print("Bemenetek: n =", n, ", m =", m, ", elek =", elek, ", s =", s)
        print("Várt eredmény:", vart_eredmeny)
        print("Kapott eredmény:", eredmeny)
        helyes_e = eredmeny == vart_eredmeny
        print(f"Helyes? {'✓' if helyes_e else '✗'}")
        
        if not helyes_e:
            print(f"   HIBA: Az eredmény nem egyezik! Várt: {vart_eredmeny}, Kapott: {eredmeny}")

if __name__ == "__main__":
    print("BFS Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()
