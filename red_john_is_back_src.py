def is_prime(n):
    # nem primszam, hamissal terunk vissza
    if n <= 1:
        return False
    # 2-tol az n negyzetgyokeig iteralunk 
    for i in range(2, int(n ** 0.5) + 1):
        # ha maradek nelkul oszthato, biztosan nem prim
        if n % i == 0:
            return False
    return True

def count_primes_up_to(M):
    # megszamoljuk, hogy mennyi prim van
    primek = 0
    for i in range(M + 1):
        if is_prime(i):
            primek += 1
    return primek

def redJohn(n):
    lefedesek = [0] * (n + 1)
    # alapertelmezett ertek, 0 hosszusaga fal lefedese
    lefedesek[0] = 1
    
    # kiszamoljuk minden i hosszusagu falra, az osszes lefedesi modot
    for i in range(1, n + 1):
        # kezdetben feltetelezzuk, hogy i hosszu fal lefedheto 1x4-es fallal (fuggoloegesen), az elozo (i-1) falhoz hozzadva
        lefedesek[i] = lefedesek[i - 1]
        # ha a fal hossza legalabb 4, akkor vizszintesen is elhelyezheto 4x1 tegla
        if i >= 4:
            lefedesek[i] += lefedesek[i - 4]
    
    M = lefedesek[n]
    # visszaterunk a lefedesi modok lehetseges szamaval
    return count_primes_up_to(M)

if __name__ == "__main__":
    input_data = input().split()
    t = int(input_data[0])
    test_esetek = list(map(int, input_data[1:]))

    for n in test_esetek:
        print(redJohn(n))