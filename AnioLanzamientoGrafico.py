import pandas as pd
import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors
def anio_lanzamiento():
    df = pd.read_csv("./archivos/juegos_general.csv")
    # Se crea nuevo campo para cantidad_juegos
    df['cantidad_juegos'] = 1

    # Se agrupan por año lanzamiento y se van sumando los juegos de cada año
    df = df.groupby(['anio_lanzamiento']).cantidad_juegos.count().reset_index()
    df = df.set_index('anio_lanzamiento')  # Se utiliza el año de lanzamiento como nuevo indice

    # Al tener el año de lanzamiento como indice y un unico campo con la cantidad de juegos, se grafica en un grafico de barras.
    df.plot(kind="bar", figsize=(8, 7))

    # Se establece el grafico de barras como primera figura.
    plot1 = plt.figure(1)
    print("Anio lanzamiento")
