from simplified_chess_engine_src import simplifiedChessEngine

def run_teszt_esetek():
    # Tesztesetek: (fehérek, feketék, lepesek, vart_eredmeny)
    teszt_esetek = [
        ([("Q", "A", "1")], [("Q", "C", "3")], 2, "IGEN"),
        ([("Q", "A", "1")], [("Q", "D", "4")], 3, "IGEN"),
        ([("Q", "A", "1")], [("Q", "D", "4")], 1, "IGEN"),
        ([("Q", "A", "1")], [("Q", "B", "2")], 1, "IGEN"),
        ([("N", "B", "1")], [("Q", "C", "3")], 2, "NEM"),
        ([("Q", "A", "1"), ("R", "B", "2"), ("B", "C", "3")], [("Q", "D", "4")], 2, "IGEN"),
        ([("Q", "A", "1"), ("R", "D", "4")], [("Q", "D", "1")], 3, "IGEN"),
        ([("Q", "A", "1"), ("R", "B", "2"), ("N", "C", "3"), ("B", "D", "4"), ("Q", "C", "2")], 
         [("Q", "D", "4"), ("R", "A", "3"), ("N", "D", "2"), ("B", "A", "4"), ("Q", "C", "1")], 6, "NEM"),
        ([("N", "A", "1")], [("Q", "D", "4")], 2, "NEM"),
        ([("Q", "A", "1"), ("R", "B", "2"), ("N", "C", "3"), ("B", "D", "4"), ("Q", "A", "4")], 
         [("Q", "D", "4"), ("R", "A", "3"), ("N", "D", "2"), ("B", "A", "4"), ("Q", "B", "3")], 6, "NEM"),
    ]
    
    for i, teszt in enumerate(teszt_esetek, 1):
        feherek, feketek, lepesek, vart_eredmeny = teszt
        eredmeny = simplifiedChessEngine(feherek, feketek, lepesek)
        
        print(f"\nTeszt #{i} eredmények:")
        print("Bemenetek: fehérek =", feherek, ", feketék =", feketek, ", lépések =", lepesek)
        print("Várt eredmény:", vart_eredmeny)
        print("Kapott eredmény:", eredmeny)
        helyes_e = eredmeny == vart_eredmeny
        print(f"Helyes? {'✓' if helyes_e else '✗'}")
        
        if not helyes_e:
            print(f"   HIBA: Az eredmény nem egyezik! Várt: {vart_eredmeny}, Kapott: {eredmeny}")

if __name__ == "__main__":
    print("simplifiedChessEngine Teszt esetek futtatása")
    print("=" * 50)
    run_teszt_esetek()
