from red_john_is_back_src import redJohn

def run_teszt_esetek():
    teszt_esetek = [
        (1, 1, 0),                  
        (2, 2, 3, 0, 0),            
        (3, 4, 5, 6, 1, 2, 2),     
        (4, 7, 8, 9, 10, 3, 4, 4, 6), 
        (5, 11, 12, 13, 14, 15, 8, 9, 11, 15, 19), 
        (6, 16, 17, 18, 19, 20, 25, 24, 32, 42, 53, 68, 269), 
        (7, 21, 22, 23, 24, 25, 26, 27, 91, 119, 155, 204, 269, 354, 462), 
        (8, 30, 31, 32, 33, 34, 35, 36, 37, 1077, 1432, 1912, 2543, 3385, 4522, 6048, 8078), 
        (9, 38, 39, 40, 17, 26, 31, 13, 32, 4, 10794, 14475, 19385, 32, 354, 1432, 11, 1912, 1), 
        (10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 1, 2, 4, 6, 9, 15, 24, 42, 68) 
    ]
    
    for i, test_eset in enumerate(teszt_esetek, 1):
        try:
            t = test_eset[0]  
            n_esetek = test_eset[1:t+1]  
            vart_kimenetek = test_eset[t+1:]  
            
            print(f"\nTeszt #{i} eredmények:")
            print("Bemenetek:", " ".join(map(str, [t] + list(n_esetek))))

            for n, vart_eredmeny in zip(n_esetek, vart_kimenetek):
                eredmeny = redJohn(n)
                helyes_e = eredmeny == vart_eredmeny
                
                print(f"\n   n = {n}")
                print(f"   Várt eredmény: {vart_eredmeny}")
                print(f"   Kapott eredmény: {eredmeny}")
                print(f"   Helyes? {'✓' if helyes_e else '✗'}")
                
                if not helyes_e:
                    print(f"   HIBA: Az eredmény nem egyezik! Várt: {vart_eredmeny}, Kapott: {eredmeny}")
                
        except Exception as e:
            print(f"\nTeszt #{i} HIBA:")
            print(f"Input: {' '.join(map(str, [t] + list(n_esetek)))}")
            print(f"Kivétel történt: {str(e)}")

if __name__ == "__main__":
    print("Red John - Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()