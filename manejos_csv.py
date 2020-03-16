# manejo de grandes volumenes de datos (archivos CSV)
import pandas
import numpy

datos = pandas.read_csv('meta/sars_2003_complete_dataset_clean.csv')
print(datos.info())

print("\n" * 2)

# muestra las contenido
print("CONTENIDO")
print(datos.head())
print("\n" * 2)

df = pandas.DataFrame(datos)

print("DATAFRAME")
print(df)
print("\n" * 2)

# reemplaza por 0 los NaN
df = df.replace(numpy.nan, '0')

print("DATOS SIN NAN")

print(df.info())
print("\n" * 2)

print("ESTADISTICAS SIN NAN")
print(df.describe())
print("\n" * 2)

#solo numeros
print("ESTADISTICAS SOLO NUMEROS")
print(df.describe(include=[numpy.number]))
print("\n" * 2)

#se reemplazan los valores null por 0
df = df.replace("N/A", "0")
df = df.replace("NR", "0")

print("ESTADISTICAS SIN NULL")
print(df.describe())
print("\n" * 2)

#encabezados
print("ENCABEZADOS")
print(list(df))
print("\n" * 2)