# Visualização de dados em Python
from matplotlib import pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 2]
z = [200, 130, 280, 330, 110]

titulo = "Scatterplot: Gráfico de dispersão" 
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="#000000", linestyle=":")
plt.scatter(x, y, label = "Pontos", color= "#22B573", marker="h", s=z)
plt.legend()

plt.show()
plt.savefig("figura4.png", dpi=300)