def simplifiedChessEngine(feherek, feketek, lepesek):
    tabla_merete = 4 
     # Feher babuk helyei es tipusaik tarolasa
    feher_babuk = {} 
    # Fekete babuk helyei es tipusaik tarolasa
    fekete_babuk = {}  
    
    # Feher babuk beolvasasa es pozicionalasa a tablazatban
    for babu in feherek:
        babu_tipus, oszlop, sor = babu 
        # Oszlop konvertalasa indexre
        oszlop_id = ord(oszlop) - ord('A')  
        # Sor konvertalasa indexre
        sor_id = int(sor) - 1  
        # Babut es poziciojat hozzaadjuk
        feher_babuk[(oszlop_id, sor_id)] = babu_tipus  
    
    # Fekete babuk beolvasasa es pozicionalasa a tablazatban
    for babu in feketek:
        babu_tipus, oszlop, sor = babu
        oszlop_id = ord(oszlop) - ord('A')
        sor_id = int(sor) - 1
        fekete_babuk[(oszlop_id, sor_id)] = babu_tipus

    # Ellenorzi, hogy egy pozicio ervenyes-e a tablan
    def poz_valid_e(poz):
        return 0 <= poz[0] < tabla_merete and 0 <= poz[1] < tabla_merete

    # Ellenorzi, hogy egy utvonal tiszta-e (nincs akadaly)
    def utvonal_tiszta_e(start_poz, veg_poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk):
         # X iranyu tavolsag
        tav_x = veg_poz[0] - start_poz[0] 
        # Y iranyu tavolsag
        tav_y = veg_poz[1] - start_poz[1]  
        
        # Ha a lovag lep, akkor automatikusan tiszta
        if abs(tav_x * tav_y) == 2:  
            return True
        
        # Lepesek szama
        lepesek = max(abs(tav_x), abs(tav_y))  
         # Ha nincs lepes, automatikusan tiszta lesz
        if lepesek == 0: 
            return True
        
        # Mozgasi irany x tengelyen
        tav_x = tav_x // lepesek if lepesek > 0 else 0 
        # Mozgasi irany y tengelyen
        tav_y = tav_y // lepesek if lepesek > 0 else 0  
        
        jelenlegi_poz = start_poz
        for _ in range(1, lepesek):
             # Kovetkezo pozicio
            jelenlegi_poz = (jelenlegi_poz[0] + tav_x, jelenlegi_poz[1] + tav_y) 
             # Ha babut talal, visszaterunk hamissal
            if jelenlegi_poz in jelenlegi_feher_babuk or jelenlegi_poz in jelenlegi_fekete_babuk:
                return False 
        return True

    # Babu mozgasi lehetosegeit adja vissza egy adott poziciobol
    def get_babu_lepesek(babu_tipus, poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk):
        lepesek = []
        # Ha huszar
        if babu_tipus == 'N':  
            iranyok = [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)
            ]
            for tav_x, tav_y in iranyok:
                uj_poz = (poz[0] + tav_x, poz[1] + tav_y)
                if poz_valid_e(uj_poz):
                    lepesek.append(uj_poz)
        
        # Ha vezer
        elif babu_tipus == 'Q':  
            iranyok = [(0,1), (1,0), (0,-1), (-1,0), 
                         (1,1), (1,-1), (-1,1), (-1,-1)]
            for tav_x, tav_y in iranyok:
                for i in range(1, tabla_merete):
                    uj_poz = (poz[0] + tav_x * i, poz[1] + tav_y * i)
                    if not poz_valid_e(uj_poz):
                        break
                    if not utvonal_tiszta_e(poz, uj_poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk):
                        break
                    lepesek.append(uj_poz)
        
        # Ha bastya
        elif babu_tipus == 'R':  
            iranyok = [(0,1), (1,0), (0,-1), (-1,0)]
            for tav_x, tav_y in iranyok:
                for i in range(1, tabla_merete):
                    uj_poz = (poz[0] + tav_x * i, poz[1] + tav_y * i)
                    if not poz_valid_e(uj_poz):
                        break
                    if not utvonal_tiszta_e(poz, uj_poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk):
                        break
                    lepesek.append(uj_poz)
        
         # Ha futar
        elif babu_tipus == 'B': 
            iranyok = [(1,1), (1,-1), (-1,1), (-1,-1)]
            for tav_x, tav_y in iranyok:
                for i in range(1, tabla_merete):
                    uj_poz = (poz[0] + tav_x * i, poz[1] + tav_y * i)
                    if not poz_valid_e(uj_poz):
                        break
                    if not utvonal_tiszta_e(poz, uj_poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk):
                        break
                    lepesek.append(uj_poz)
        
        return lepesek

    # Ellenorzi, hogy nyerhet-e a feher adott szamu lepesbol
    def nyerhet_e(jelenlegi_feher_babuk, jelenlegi_fekete_babuk, hatramarado_lepesek, feher_kore):
        # Ha nincs tobb lepes, nem nyerhet
        if hatramarado_lepesek <= 0: 
            return False
            
        # Fekete es feher vezer poziciojanak meghatarozasa
        feketer_verzer_poz = None
        feher_vezer_poz = None
        for poz, babu in jelenlegi_fekete_babuk.items():
            if babu == 'Q':
                feketer_verzer_poz = poz
                break
        for poz, babu in jelenlegi_feher_babuk.items():
            if babu == 'Q':
                feher_vezer_poz = poz
                break
        
        # Ha nincs fekete vezer, feher nyer
        if feketer_verzer_poz is None:  
            return True
        # Ha nincs feher vezer, nem nyerhet
        if feher_vezer_poz is None:  
            return False
            
        if feher_kore:  
            for poz, babu_tipus in jelenlegi_feher_babuk.items():
                lehetseges_lepesek = get_babu_lepesek(babu_tipus, poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk)
                
                for uj_poz in lehetseges_lepesek:
                    if uj_poz in jelenlegi_feher_babuk:
                        continue
                        
                    uj_feher_babuk = jelenlegi_feher_babuk.copy()
                    uj_fekete_babuk = jelenlegi_fekete_babuk.copy()
                    
                    del uj_feher_babuk[poz]
                    uj_feher_babuk[uj_poz] = babu_tipus
                    
                    if uj_poz in uj_fekete_babuk:
                        if uj_poz == feketer_verzer_poz:
                            return True
                        del uj_fekete_babuk[uj_poz]
                    
                    if nyerhet_e(uj_feher_babuk, uj_fekete_babuk, hatramarado_lepesek - 1, False):
                        return True
        else:  
            for poz, babu_tipus in jelenlegi_fekete_babuk.items():
                lehetseges_lepesek = get_babu_lepesek(babu_tipus, poz, jelenlegi_feher_babuk, jelenlegi_fekete_babuk)
                
                for uj_poz in lehetseges_lepesek:
                    if uj_poz in jelenlegi_fekete_babuk:
                        continue
                        
                    uj_feher_babuk = jelenlegi_feher_babuk.copy()
                    uj_fekete_babuk = jelenlegi_fekete_babuk.copy()
                    
                    del uj_fekete_babuk[poz]
                    uj_fekete_babuk[uj_poz] = babu_tipus
                    
                    if uj_poz in uj_feher_babuk:
                        if uj_poz == feher_vezer_poz:
                            return False
                        del uj_feher_babuk[uj_poz]
                    
                    if not nyerhet_e(uj_feher_babuk, uj_fekete_babuk, hatramarado_lepesek - 1, True):
                        return False
            return True
                    
        return False

    # Eredmeny meghatarozasa es visszateres
    eredmeny = nyerhet_e(feher_babuk, fekete_babuk, lepesek, True)
    return "IGEN" if eredmeny else "NEM"

if __name__ == "__main__":
    g = int(input().strip())
    eredmenyek = []

    for _ in range(g):
        w, b, m = map(int, input().strip().split())
        
        feherek = []
        for _ in range(w):
            tipus, oszlop, sor = input().strip().split()
            feherek.append((tipus, oszlop, sor))
        
        feketek = []
        for _ in range(b):
            tipus, oszlop, sor = input().strip().split()
            feketek.append((tipus, oszlop, sor))
        
        eredmeny = simplifiedChessEngine(feherek, feketek, m)
        eredmenyek.append(eredmeny)
    
    for eredmeny in eredmenyek:
        print(eredmeny)