from sympy import symbols, sqrt

class EllipticCurve:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def equation(self):
        """Devuelve la ecuación de la curva."""
        x, y = symbols('x y')
        return Eq(y**2, x**3 + self.a*x + self.b)
    
    def has_rational_point(self, x):
        """
        Verifica si existe un punto racional en la curva con coordenada x dada.
        """
        y_squared = x**3 + self.a*x + self.b
        y_value = sqrt(y_squared)
        return y_value.is_rational

    def get_rational_points(self, limit=100):
        """Busca puntos racionales en la curva hasta un cierto límite para x."""
        points = []
        for x in range(-limit, limit + 1):
            y_squared = x**3 + self.a*x + self.b
            y_value = sqrt(y_squared)
            if y_value.is_rational:
                points.extend([(x, y_value), (x, -y_value)])
        return points

    def __str__(self):
        return f"Elliptic Curve defined by: {self.equation()}"

if __name__ == "__main__":
    curve = EllipticCurve(1, 1)
    print(curve)
    
    points = curve.get_rational_points(limit=100)
    print("\nPuntos racionales:")
    for point in points:
        print(point)
