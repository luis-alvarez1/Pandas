#importa pandas y numpy
import pandas
import numpy

#se leen los datos y se asignan a una variable
datos = pandas.read_csv("meta/sars_2003_complete_dataset_clean.csv")
dataframe = pandas.DataFrame(datos) #se crea el dataframe

#se exporta el dataframe como CSV
dataframe.reset_index().to_csv('meta/DatosExportadosSARS.csv',header=True,index=False)

#Se itera sobre los paises
datos.set_index('Country' , inplace=True)

#se tra info del indice (pais) específico
dataframe = datos.loc['Slovenia']

# se exporta esa info 
dataframe.reset_index().to_csv('meta/SloveniaSARS.csv',header=True,index=False)

#selecciona solo los paises que terminen en 'y'

dataframe2 = datos.loc[datos['Date'].str.endswith('3')]

dataframe2.reset_index().to_csv('meta/DateSelectionSARS.csv',header=True,index=False)
