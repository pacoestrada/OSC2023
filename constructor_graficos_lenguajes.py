import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo CSV
df = pd.read_csv('IDEs-Lenguajes.csv')

# Convertir todos los lenguajes a minúsculas y eliminar espacios al principio y al final
df['Lenguaje'] = df['Lenguaje'].str.lower().str.strip()

# Contar las frecuencias de los diferentes lenguajes
lenguaje_counts = df['Lenguaje'].value_counts()

# Crear una figura con dos paneles
fig, ax = plt.subplots(1, 2, figsize=(15, 7))

# Crear una lista de colores para las barras. Los colores se repetirán si hay más lenguajes que colores
colors = plt.get_cmap('tab20').colors

# Diagrama de sectores en el panel izquierdo
wedges, texts, autotexts = ax[0].pie(lenguaje_counts, labels=lenguaje_counts.index, autopct='%1.1f%%', colors=colors)

# Añadir una leyenda
ax[0].legend(wedges, lenguaje_counts.index, title="Lenguajes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax[0].set_title('Diagrama de Sectores de Lenguajes de Programación')

# Diagrama de barras en el panel derecho
bars = ax[1].bar(lenguaje_counts.index, lenguaje_counts, color=colors[:len(lenguaje_counts)])
ax[1].set_title('Diagrama de Barras de Lenguajes de Programación')
ax[1].set_xlabel('Lenguajes')
ax[1].set_ylabel('Frecuencia')
plt.xticks(rotation=90)

# Añadir un título general a la figura
titulo = 'Representación de los lenguajes más usados según las entrevistas de OSC2023'
fig.suptitle(titulo, fontsize=16, y=1.05)
# Para resaltar 'OSC2023', cambiamos su color y tamaño
fig.text(.5, .96, titulo, ha='center', va='bottom', color='darkblue', size=20)

# Mostrar la figura
plt.tight_layout()
plt.show()
