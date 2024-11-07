from goodland_electricity_src import pylons

def run_teszt_esetek():
    # Tesztesetek: (k, arr, vart_eredmeny)
    teszt_esetek = [
        (1, [1] * 10, 10),                       
        (2, [0, 1, 0, 0, 1, 0, 0, 1, 0, 1], 4),   
        (3, [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 4),  
        (3, [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1], 3), 
        (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], -1),  
        (5, [1] + [0] * 99 + [1] * 10, -1),        
        (3, [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1], 4), 
        (4, [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0], 3), 
        (100, [1] * 50 + [0] * 900 + [1] * 50, -1), 
        (500, [0] * 499 + [1] + [0] * 499, 1), 
    ]
    
    for i, teszt in enumerate(teszt_esetek, 1):
        k, arr, vart_eredmeny = teszt
        eredmeny = pylons(k, arr)
        
        print(f"\nTeszt #{i} eredmények:")
        print("Bemenetek: k =", k, ", arr =", arr)
        print("Várt eredmény:", vart_eredmeny)
        print("Kapott eredmény:", eredmeny)
        helyes_e = eredmeny == vart_eredmeny
        print(f"Helyes? {'✓' if helyes_e else '✗'}")
        
        if not helyes_e:
            print(f"   HIBA: Az eredmény nem egyezik! Várt: {vart_eredmeny}, Kapott: {eredmeny}")

if __name__ == "__main__":
    print("Goodland Electricity Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()
