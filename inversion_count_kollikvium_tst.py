from inversion_count_kollikvium_src import count_inversions

def run_teszt_esetek():
    teszt_esetek = [
        ([3, 1, 2], 2),
        ([2, 3, 8, 6, 1], 5),
        ([5, 4, 3, 2, 1], 10),
        ([1, 2, 3, 4, 5], 0),
        ([10, 9, 8, 7, 6], 10),
        ([1, 5, 3, 2, 4], 4),
        ([10, 9, 7, 8, 5, 6], 13),
        ([15, 8, 3, 5, 11, 7], 9),
        ([1, 3, 5, 2, 4, 6], 3),
        ([20, 15, 25, 5, 30, 10], 8)
    ]
    
    for i, (arr, vart_eredmeny) in enumerate(teszt_esetek, 1):
        eredmeny = count_inversions(arr)
        
        print(f"\nTeszt #{i} eredmények:")
        print("Bemenet:", arr)
        print("Várt eredmény:", vart_eredmeny)
        print("Kapott eredmény:", eredmeny)
        helyes_e = eredmeny == vart_eredmeny
        print(f"Helyes? {'✓' if helyes_e else '✗'}")
        
        if not helyes_e:
            print(f"   HIBA: Az eredmény nem egyezik! Várt: {vart_eredmeny}, Kapott: {eredmeny}")

if __name__ == "__main__":
    print("Inverziók számoló Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()