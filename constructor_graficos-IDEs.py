import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo CSV
df = pd.read_csv('IDEs-Lenguajes.csv')

# Convertir todos los IDEs a minúsculas para uniformidad
df['IDE'] = df['IDE'].str.lower().str.strip()

# Contar las frecuencias de los diferentes IDEs
ide_counts = df['IDE'].value_counts()

# Crear una figura con dos paneles
fig, ax = plt.subplots(1, 2, figsize=(15, 7))

# Crear una lista de colores para las barras. Los colores se repetirán si hay más IDEs que colores
colors = plt.get_cmap('tab20').colors

# Diagrama de sectores en el panel izquierdo
wedges, texts, autotexts = ax[0].pie(ide_counts, labels=ide_counts.index, autopct='%1.1f%%', colors=colors)

# Añadir una leyenda, moviéndola ligeramente a la derecha
ax[0].legend(wedges, ide_counts.index, title="IDEs", loc="center left", bbox_to_anchor=(1.1, 0, 0.5, 1))
ax[0].set_title('Diagrama de Sectores de IDEs de Programación')

# Diagrama de barras en el panel derecho
bars = ax[1].bar(ide_counts.index, ide_counts, color=colors[:len(ide_counts)])
ax[1].set_title('Diagrama de Barras de IDEs de Programación')
ax[1].set_xlabel('IDEs')
ax[1].set_ylabel('Frecuencia')
plt.xticks(rotation=90)

# Añadir un título general a la figura
titulo = 'Representación de los IDEs más usados según las entrevistas de OSC2023'
fig.suptitle(titulo, fontsize=16, y=1.05)
# Para resaltar 'OSC2023', cambiamos su color y tamaño
fig.text(.5, .96, titulo, ha='center', va='bottom', color='darkblue', size=20)

# Mostrar la figura
plt.tight_layout()
plt.show()



