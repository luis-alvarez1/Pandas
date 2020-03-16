# importar pandas
import pandas
import numpy
# se define un diccionario con las columnas y las filas del dataframe
# el contenido de las columnas se deben almacenar en listas (arrays)
DATOS1 = {
    'nombre': ['Luis', 'Maria', 'Jose', 'Nicole'],
    'calificacion': ['3,5', '4,2', '2.6', '3,0'],
    'facultad': ['Ing', 'FCAC', 'Salud', 'Edu'],
    'semestre': ['5', '2', '4', '9']
}

# se convierte el diccionario a un dataframe con pandas

dataframe1 = pandas.DataFrame(DATOS1)

print("DATAFRAME1")
print(dataframe1)
print("\n" * 2)
# not available data

DATOS2 = {
    'nombre': ['Luis', 'N/A', 'Jose', 'Nicole'],
    'calificacion': ['3.5', '4.2', '2.6', numpy.nan],
    'facultad': ['N/A', 'FCAC', 'Salud', 'Lic'],
    'semestre': ['5', '2', 'N/A', '9']
}

dataframe2 = pandas.DataFrame(DATOS2)

print("DATAFRAME2")
print(dataframe2)
print("\n" * 2)

print("INFO DATOS NULL")
print(dataframe2.info())
print("\n" * 2)

# estadisticas info
print("ESTADISTICAS")
print(dataframe2.describe())
print("\n" * 2)

# nuevo dataframe que depende del antiguo dataframe
nuevodataframe = pandas.DataFrame(dataframe2)

# rellenar con 0 los valore null

#metodo 1
nuevodataframe = nuevodataframe.replace(numpy.nan, 0)

print("NUEVO DATAFRAME")
print(nuevodataframe)
print("\n" * 2)

# nuevo dataframe que depende del antiguo dataframe
nuevodataframe2 = pandas.DataFrame(dataframe2)

'''dropna(): Parameters:

axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String.

how: how takes string value of two kinds only (‘any’ or ‘all’). ‘any’ drops the row/column if ANY value is Null and ‘all’ drops only if ALL values are null.

thresh: thresh takes integer value which tells minimum amount of na values to drop.

subset: It’s an array which limits the dropping process to passed rows/columns through list.

inplace: It is a boolean which makes the changes in data frame itself if True.'''

#elimina todo lo que sea null
# nuevodataframe2 = nuevodataframe2.dropna(how='any', inplace=True)

print("NUEVO DATFRAME SIN NULL")
print(nuevodataframe2)
print("\n" * 2)



nuevodataframe3 = pandas.DataFrame(dataframe2)

'''
fillna(): Parameters:
value : Static, dictionary, array, series or dataframe to fill instead of NaN.

method : Method is used if user doesn’t pass any value. Pandas has different methods like bfill, backfill or ffill which fills the place with value in the Forward index or Previous/Back respectively.

axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String

inplace: It is a boolean which makes the changes in data frame itself if True.

limit : This is an integer value which specifies maximum number of consequetive forward/backward NaN value fills.

downcast : It takes a dict which specifies what dtype to downcast to which one. Like Float64 to int64.

**kwargs : Any other Keyword arguments
'''

#metodo 2
nuevodataframe3.fillna(0, inplace=True)

print("RELLENANDO CON 0")
print(nuevodataframe3)
print("\n" * 2)

#estadisticas luego del remplazo
print("ESTADISTICAS LUEGO DE EL REEMPLAZO")
print(nuevodataframe3.describe())
print("\n" * 2)

#convierte a numeros float
nuevodataframe2['calificacion'] = nuevodataframe2.calificacion.astype(float)

print("LUEGO DE CONVERTIR A INT")
print(nuevodataframe2.describe())
print("\n" * 2)

#estadisticas individuales

print("promedio", nuevodataframe2['calificacion'].mean())