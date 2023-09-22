from sympy import symbols, sqrt, Eq

class EllipticCurve:
    """
    Una curva elíptica, en términos simples, es un conjunto de puntos que satisface una ecuación 
    de la forma y^2 = x^3 + ax + b. Aunque el nombre sugiere una relación con elipses, 
    las curvas elípticas en realidad no tienen relación directa con ellas. Estas curvas tienen 
    propiedades y estructuras matemáticas especiales que las hacen útiles en diversos campos, 
    como la criptografía y la teoría de números.

    Esta clase representa una curva elíptica en su forma de Weierstrass. 
    
    La conjetura de Birch y Swinnerton-Dyer sugiere que hay una relación entre el número de 
    soluciones racionales de esta curva y ciertas propiedades de una función matemática llamada 
    función L. Esta conjetura trata, en esencia, sobre la cantidad de soluciones que 
    puede tener la ecuación de la curva.
    
    Atributos:
    a, b (int, int): Coeficientes de la ecuación de la curva.
    """
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def equation(self):
        """Devuelve la ecuación de la curva en su forma de Weierstrass."""
        x, y = symbols('x y')
        return Eq(y**2, x**3 + self.a*x + self.b)
    
    def has_rational_point(self, x):
        """
        Verifica si existe un punto racional en la curva con coordenada x dada.
        
        Un punto racional es aquel donde tanto x como y son números racionales.
        """
        y_squared = x**3 + self.a*x + self.b
        y_value = sqrt(y_squared)
        return y_value.is_rational

    def get_rational_points(self, limit=100):
        """
        Busca puntos racionales en la curva hasta un cierto límite para x.
        
        Retorna una lista de puntos (x, y) donde x es un número entero en el rango
        [-limit, limit] y y es un número racional.
        """
        points = []
        for x in range(-limit, limit + 1):
            y_squared = x**3 + self.a*x + self.b
            y_value = sqrt(y_squared)
            if y_value.is_rational:
                points.extend([(x, y_value), (x, -y_value)])
        return points

    def __str__(self):
        return f"La ecuación {self.equation()} define una curva elíptica en su forma estándar, conocida como forma de Weierstrass."

if __name__ == "__main__":
    curve = EllipticCurve(1, 1)
    print(curve)
    
    points = curve.get_rational_points(limit=100)
    print("\nEn este caso, hemos encontrado algunos puntos racionales en la curva. Un punto racional es aquel cuyas coordenadas x y y son números racionales. Estos puntos son:")
    for point in points:
        print(point)
    print("\nLas curvas elípticas son fundamentales en la teoría de números, habiendo sido esenciales para resolver problemas históricos, como el Último Teorema de Fermat. Además, son vitales en la criptografía moderna, proporcionando sistemas criptográficos eficientes y seguros.")
