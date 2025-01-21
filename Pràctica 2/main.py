import matplotlib.pyplot as plt
from funcions import iteracions_MCD_Euclides
x = []
y = []
z = []
num=250
for i in range(1,num+1):
    for j in range(1, num+1):
        x.append(i)
        y.append(j)
        z.append(iteracions_MCD_Euclides(i,j))
plt.scatter(x, y, c=z)
plt.colorbar()
plt.show()