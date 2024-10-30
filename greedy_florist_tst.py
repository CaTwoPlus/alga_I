from greedy_florist_src import getMinimumCost

def run_teszt_esetek():
    teszt_esetek = [
        (5, 3, [2, 5, 6, 1, 4], 21),
        (3, 3, [3, 2, 1], 6),
        (3, 1, [5, 4, 3], 22), 
        (4, 2, [100, 98, 95, 93], 574),
        (3, 5, [1, 2, 3], 6),
        (10, 4, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 79),
        (5, 3, [5, 5, 5, 5, 5], 35),
        (12, 2, [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4], 329),
        (10000, 100, list(range(1, 10001)), 1692002500),
        (10, 1, list(range(10, 0, -1)), 220)
    ]
    
    for i, (n, k, c, vart_eredmeny) in enumerate(teszt_esetek, 1):
        try:
            # Elmentjuk az eredeti c listat a reszletes kiirashoz
            eredeti_c = c.copy()
            
            eredmeny = getMinimumCost(k, c)
            helyes_e = eredmeny == vart_eredmeny
            print(f"\nTeszt #{i} eredmények:")
            print(f"n = {n} (virágok száma)")
            print(f"k = {k} (barátok száma)")
            print(f"c[] = {eredeti_c}")
            print(f"Várt eredmény: {vart_eredmeny}")
            print(f"Kapott eredmény: {eredmeny}")
            print(f"Helyes? {'✓' if helyes_e else '✗'}")
            
            if not helyes_e:
                print(f"HIBA: Az eredmény nem egyezik! Várt: {vart_eredmeny}, Kapott: {eredmeny}")

        except Exception as e:
            print(f"\nTeszt #{i} HIBA:")
            print(f"n = {n}, k = {k}")
            print(f"Kivétel történt: {str(e)}")

if __name__ == "__main__":
    print("Mohó virágárus - Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()