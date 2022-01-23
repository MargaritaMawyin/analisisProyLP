import pandas as pd
import matplotlib.pyplot as plt

def genero():
    # Se crea nuevo campo para cantidad_juegos
    df = pd.read_csv("./archivos/juegos_general.csv")
    df['cantidad_juegos'] = 1

    # Se agrupan por año lanzamiento y se van sumando los juegos de cada año
    df = df.groupby(['genero']).cantidad_juegos.count().reset_index()
    df = df.set_index('genero')  # Se utiliza el año de lanzamiento como nuevo indice
    df.plot(kind="bar", figsize=(8, 7))
    print(df)
    plt.show()
