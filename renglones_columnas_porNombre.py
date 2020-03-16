import pandas
import numpy

datos = pandas.read_csv("meta/sars_2003_complete_dataset_clean.csv")

# se fija el indice
datos.set_index("Country", inplace=True)

# loc accede a ciertas columnas o filas por etiquetas o arrays
print("UK")
# se imprime todo lo relacionado al UK
print(datos.loc["United Kingdom"])
print("\n" * 2)

# columnas especificas
print("SPAIN & DEATHS")
print(datos.loc['Spain', 'Number of deaths'])
print("\n" * 2)

# columnas y renglones específicos
print("SELECCION AMPLIA")
print(datos.loc[['Germany', 'France'], [
      'Cumulative number of case(s)', 'Number of deaths']])
print("\n" * 2)

#Seleccion de rango
#los rangos no pueden ir dentro de corchetes
print("SELECCION DE RANGO")
print(datos.loc[['Germany', 'France'], 'Cumulative number of case(s)':'Number recovered'])
print("\n" * 2)

#paises que solo prensentaron una 
print("SOLO UNA MUERTE")
print(datos.loc[datos['Number of deaths'].int64.endswith('1')])
print("\n" * 2)