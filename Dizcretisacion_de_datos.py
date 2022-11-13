import numpy as np
import pandas as pd

edades = np.array([1,7,8,15,16,35,30,50,55,70,75,80])

resultado = pd.cut(edades,
                   bins=3,
                   labels=["baja","media","alta"],
                   include_lowest=True,
                   retbins=True)

print(resultado[1], "\n")
print(resultado[0].codes, "\n")
print(resultado[0].categories, "\n")
print(resultado[0].categories, "\n")
