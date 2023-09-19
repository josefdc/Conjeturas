import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_fcc_points(size):
    """
    Genera puntos en un arreglo FCC.
    
    Parámetros:
        - size (int): determina cuántas capas de esferas se deben generar.
        
    Devuelve:
        - Una lista de puntos (x, y, z) que representan los centros de las esferas.
    """
    points = []
    
    for x in range(size):
        for y in range(size):
            for z in range(size):
                points.append((x, y, z))
                if (x + y + z) % 2 == 0:  # Añade el punto central solo para celdas pares
                    points.append((x + 0.5, y + 0.5, z + 0.5))
    return points

def plot_fcc_packing(size):
    """
    Visualiza el empaquetamiento FCC de esferas.
    
    Parámetros:
        - size (int): determina cuántas capas de esferas se deben visualizar.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    points = generate_fcc_points(size)
    
    for point in points:
        ax.scatter(*point, s=100)
    
    ax.set_title('Empaquetamiento FCC')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

if __name__ == "__main__":
    plot_fcc_packing(3)
