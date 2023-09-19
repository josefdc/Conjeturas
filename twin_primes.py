def is_prime(n):
    """
    Verifica si un número es primo.
    
    Parámetros:
        - n (int): el número a verificar.
    
    Devuelve:
        - True si n es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def twin_primes(limit):
    """
    Genera una lista de primos gemelos hasta un cierto límite.
    
    Parámetros:
        - limit (int): el límite superior para buscar primos gemelos.
        
    Devuelve:
        - Una lista de tuplas, donde cada tupla contiene un par de primos gemelos.
    """
    twins = []
    for n in range(2, limit - 1):
        if is_prime(n) and is_prime(n + 2):
            twins.append((n, n + 2))
    return twins

if __name__ == "__main__":
    try:
        limit = int(input("Introduce el límite superior para buscar primos gemelos: "))
        if limit < 3:
            print("Por favor, introduce un número mayor o igual a 3.")
        else:
            pairs = twin_primes(limit)
            print(f"Pares de primos gemelos hasta {limit}:")
            for pair in pairs:
                print(pair)
    except ValueError:
        print("Por favor, introduce un número válido.")
