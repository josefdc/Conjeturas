def collatz(n):
    """Implementa la secuencia de la Conjetura de Collatz para un número entero positivo n.

    La conjetura de Collatz, también conocida como la conjetura 3n + 1, sostiene que la siguiente secuencia 
    eventualmente llegará a 1 para cualquier número entero positivo:
    1. Si n es par, divídelo por 2.
    2. Si n es impar, multiplícalo por 3 y súmale 1.

    Parámetros:
    - n (int): Número entero positivo inicial.

    Retorna:
    - list: Una lista con la secuencia de Collatz para el número n.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # Si n es par
            n = n // 2
        else:  # Si n es impar
            n = 3 * n + 1
        sequence.append(n)
    return sequence

if __name__ == "__main__": # Si se ejecuta este archivo directamente
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
