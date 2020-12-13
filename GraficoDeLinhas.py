# Visualização de dados em Python
from matplotlib import pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

titulo = "Gráfico de linhas"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Eixos
plt.plot(x, y)

plt.show()
plt.savefig("figura1.png", dpi=300)