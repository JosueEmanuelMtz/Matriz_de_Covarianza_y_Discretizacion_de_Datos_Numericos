import pandas as pd

# quitar notación científica
pd.options.display.float_format = '{:.2f}'.format

# Contexto:
#   (0) Edad,  
#   (1) Gastos mensuales en Medicina, 
#   (2) Gastos mensuales en Educación, y
#   (3) Gastos mensuales en Cacahuates

datos = {"edad" : [35, 50, 22, 45, 18, 75, 55, 20, 23, 49],
         "medicina" : [200, 1500, 150, 250, 0, 2500, 1400, 50, 0, 600],
         "educacion" : [1200, 0, 7500, 2200, 8300, 0, 0, 4900, 5100, 800],
         "cacahuates" : [10, 15, 0, 10, 20, 10, 20, 10, 15, 0]}
         
datos = pd.DataFrame(datos)
datos
datos.aggregate(["std", "var"])



import matplotlib.pyplot as plt

def subgrafica_std(datos, columna, fig, posicion): 
    ax = fig.add_subplot(1, 4, posicion)    
    
    # calculando media y desviación estándar
    media = datos[columna].mean() 
    std = datos[columna].std()
   
    # graficando datos
    ax.scatter(range(len(datos[columna])), datos[columna],
               marker="D", s=150, color="purple")
    
    # graficando media y desviación estándar 
    ax.axhline(y=media+std, color="gray", linestyle="--", linewidth=3)
    ax.axhline(y=media, color="teal", linestyle=":",  linewidth=6)
    ax.axhline(y=media-std, color="gray", linestyle="--", linewidth=3)

    # presentación de gráfica
    ax.set_title("Dev std: " + columna.capitalize(), fontsize=20)
    ax.set_xticks(range(len(datos[columna])))
    ax.get_xaxis().set_visible(False)


# Desviaciones estándar para todas las columnas    
fig = plt.figure(figsize=(18, 5))     

subgrafica_std(datos, "edad", fig, 1)
subgrafica_std(datos, "medicina", fig, 2)
subgrafica_std(datos, "educacion", fig, 3)
subgrafica_std(datos, "cacahuates", fig, 4)

plt.show()


import matplotlib.pyplot as plt

def subgrafica_std(datos, columna, fig, posicion): 
    ax = fig.add_subplot(1, 4, posicion)    
    
    # calculando media y desviación estándar
    media = datos[columna].mean() 
    std = datos[columna].std()
   
    # graficando datos
    ax.scatter(range(len(datos[columna])), datos[columna],
               marker="D", s=150, color="purple")
    
    # graficando media y desviación estándar 
    ax.axhline(y=media+std, color="gray", linestyle="--", linewidth=3)
    ax.axhline(y=media, color="teal", linestyle=":",  linewidth=6)
    ax.axhline(y=media-std, color="gray", linestyle="--", linewidth=3)

    # presentación de gráfica
    ax.set_title("Dev std: " + columna.capitalize(), fontsize=20)
    ax.set_xticks(range(len(datos[columna])))
    ax.get_xaxis().set_visible(False)


# Desviaciones estándar para todas las columnas    
fig = plt.figure(figsize=(18, 5))     

subgrafica_std(datos, "edad", fig, 1)
subgrafica_std(datos, "medicina", fig, 2)
subgrafica_std(datos, "educacion", fig, 3)
subgrafica_std(datos, "cacahuates", fig, 4)

plt.show()