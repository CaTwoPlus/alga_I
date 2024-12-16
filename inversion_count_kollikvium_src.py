# Merge sort alapon számoljuk az inverziókat
def merge_count_split_inv(arr, temp_arr, left, right):
    # Ha csak egy elemre redukálódott, már nem kell összehasonlítani
    if left == right:
        return 0
    # Középső elem számolása, tömb két felére osztva
    mid = (left + right) // 2
    inv_count = merge_count_split_inv(arr, temp_arr, left, mid)
    # Tömb hívása rekurzívan, mindkét félre
    inv_count += merge_count_split_inv(arr, temp_arr, mid + 1, right)
    # Inverziók összeolvasztása
    inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    # Visszatérünk az inverziók számával a teljes szakaszra
    return inv_count
 
def merge_and_count(arr, temp_arr, left, mid, right):
    # i, j, k - aktuális indexek
    i = left   
    j = mid + 1
    k = left  
    # számláló
    inv_count = 0
    
    # Addig fut, amíg mindkét részben vannak elemek
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            # Átmeneti tömbbe való másolás, i léptetése
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Ekkor az összes bal oldali elem inverziónak számít
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # Átmásoljuk a a bal oldal maradék elemeit
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    # Átmásoljuk a jobb oldal maradék elemeit is
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # Eredeti tömbbe való visszamásolás
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count
 
# Inverziók számolása
def count_inversions(arr):
    n = len(arr)
    # Segédtömb az összeolvasztáshoz
    temp_arr = [0] * n
    # Számlálás rekurzívan
    return merge_count_split_inv(arr, temp_arr, 0, n - 1)
 
def main():
    # Tesztesetek száma
    t = int(input().strip())  
    input()  
    for _ in range(t):
        # Tömb mérete
        n = int(input().strip()) 
        # Tömb elemei
        arr = []
        for _ in range(n):
            arr.append(int(input().strip()))  
        # Ha nem az utolsó teszteset, üres sor átugrása
        if _ != t - 1: 
            input()  
        print(count_inversions(arr)) 
 
if __name__ == "__main__":
    main()