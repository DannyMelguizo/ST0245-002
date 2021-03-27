import pandas as pd

dataVertices = pd.read_csv('Vertices.csv')
print(dataVertices.head())

dataArcos = pd.read_csv('Arcos.csv')
print(dataArcos.head())

diccArcos = {}

print("\n\n")
for i in dataArcos.index:
    
    diccArcos[(dataArcos.iloc[i]['ID'],dataArcos.iloc[i]['ID1'])] = dataArcos.loc[i]
    
print("El diccionario de los arcos es:")
print("\n",diccArcos,"\n")

diccVert = {}
for i in dataVertices.index:
    diccVert[(dataVertices.iloc[i]['ID'])] = dataVertices.loc[i]

print("El diccionario de los vertices es:")
print("\n",diccVert,"\n")
