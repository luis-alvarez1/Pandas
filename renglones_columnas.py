#importa panda y numpy
import pandas
import numpy

dataframe = pandas.read_csv("meta/sars_2003_complete_dataset_clean.csv")

print(dataframe.info())
print("\n" * 2)

#primeros 5 renglones

print("PRIMEROS 5 RENGLONES")
print(dataframe.head())
print("\n" * 2)

#otros primeros 5 renglones

print("FUNCION ILOC")
print(dataframe.iloc[0:5])
print("\n" * 2)

#seleccionar algunas filas 

#df.iloc[[<renglones>], [<columnas>]]
print("RENGLONES ESPECIFICOS")
print(dataframe.iloc[[0,23,34,586]])
print("\n" * 2)

#colmunas
print("COLUMNAS ESPECIFICAS")
print(dataframe.iloc[:,1:3])
print("\n" * 2)

#rangos
print("RANGOS")
print(dataframe.iloc[0:400,2:4])
print("\n" * 2)