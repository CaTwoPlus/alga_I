from recursive_digit_sum_src import superDigit

def run_teszt_esetek():
    teszt_esetek = [
        ("148", 3, 3),            
        ("9875", 4, 8),            
        ("123", 3, 9),             
        ("999", 1, 9),            
        ("1", 5, 1),              
        ("45", 10, 9),              
        ("567", 100, 9),           
        ("91827364", 2, 9),         
        ("9999999999", 1, 9),       
        ("12345", 5, 3)            
    ]
    
    for i, (n, k, vart_eredmeny) in enumerate(teszt_esetek, 1):
        try:
            eredmeny = superDigit(n, k)
            helyes_e = eredmeny == vart_eredmeny
            
            print(f"\nTeszt #{i} eredmények:")
            print(f"n = {n} (eredeti szám)")
            print(f"k = {k} (ismétlések száma)")
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
    print("Super Digit - Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()