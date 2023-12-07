import pandas as pd
import matplotlib.pyplot as plt

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}


df = pd.DataFrame(data)


df['nota'] = pd.to_numeric(df['nota'])

# Establecer el orden deseado para las materias
orden_materias = ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']
df['materia'] = pd.Categorical(df['materia'], categories=orden_materias, ordered=True)

plt.figure(figsize=(8, 6))
df.boxplot(column='nota', by='materia', figsize=(10,6))
plt.title('Distribución de Notas de Estudiantes por Materia')
plt.xlabel('Materias')
plt.ylabel('Notas')
plt.suptitle('')  # Elimina el título automático generado por pandas
plt.xticks(rotation=45) 
plt.grid(True)

aprobados = df[df['aprobado'] == 'Sí']
no_aprobados = df[df['aprobado'] == 'No']
cantidad_aprobados = len(aprobados)
cantidad_no_aprobados = len(no_aprobados)

# Crear un pie chart
labels = ['Aprobados', 'No Aprobados']
sizes = [cantidad_aprobados, cantidad_no_aprobados]
colors = ['#ff9999', '#66b3ff']
plt.figure(figsize=(8, 6))
plt.pie([cantidad_aprobados, cantidad_no_aprobados], labels=['Aprobados', 'No Aprobados '], colors=['#ff9999', '#66b3ff'], autopct='%1.1f%%')
plt.title('Distribución de Estudiantes Aprobados y No Aprobados')
plt.axis('equal')
plt.show()