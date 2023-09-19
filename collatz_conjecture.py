def collatz(n):
    """Función que implementa la conjetura de Collatz."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # Si n es par
            n = n // 2
        else:  # Si n es impar
            n = 3 * n + 1
        sequence.append(n)
    return sequence

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Introduce un número positivo entero (0 para salir): "))
            if num < 0:
                print("Por favor, introduce un número positivo.")
            elif num == 0:
                break
            else:
                result = collatz(num)
                print(f"Secuencia de Collatz para {num}: {result}")
                print(f"La secuencia tiene {len(result)} números.")
        except ValueError:
            print("Por favor, introduce un número entero positivo.")
