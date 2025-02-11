### Pràctica 4: Resolució d'Equacions amb el Mètode de la Bisecció

### 1. Descripció del Problema

- En aquesta pràctica, desenvolupareu un programa en Python que utilitza el mètode de la bisecció per resoldre equacions de la formaf(x)=0, on f(x)és una funció contínua. També es proposa implementar una millora opcional amb el mètode de la falsa posició.

### 2. Anàlisi del Problema i Estratègia de solució

- En aquesta pràctica primer de tot vaig entendre que era el mètode de la bisseció, despres vaig pensar en com hem ficaria a fer les funcions d'aquesta pràctica. Vaig pensar que acabaria el codi a classe i a casa faria el readme.

### 3. Implementació

- Aquesta funció representa la recta:
-  def f(x):
-   return 2*x-4

- Aquesta comprova si el Teorema de Bolzano es compleix en l'interval [a,b]
- def compleix_bolzano(f, a, b):
-    if f(a) * f(b) < 0:
-        return True
-    return False
- Aquesta funció aplica el metòde de bissecció, per poder trobar la arrel d'una funció.  
- def biseccio(f, a, b, tol):
-    i = 0
-    xm = (a + b) / 2
-    while abs(f(xm)) > tol:
-        if f(a) * f(xm) < 0:
-            b = xm
-        else:
-            a = xm
-       i += 1
-        xm = (a + b) / 2
-    return xm, f(xm), i

### 4. Resultats Obtinguts

- Això es el que surt quan li dono play:
- Introdueix el valor de a: 4
- Introdueix el valor de b: -4
- Dades d'entrada: 
- def f(x):       
-    return 2*x-4
-    None
- Tolerància:1e-10
- Valor a: 4.0.
- Valor b: -4.0.
- Resultat d'aplicar el Mètode de la Bisecció: 
- Solució aproximada: x_b = 2.0.
- f(x_b) = 0.0.
- Nombre d'iteracions: 1.

### 5. Anàlisi dels resultats i conclusions

- Doncs els resultats et donen la def f(x), el valor de a i de b si compleix bolzano. I despés de aplicar el mètode de bissecció la solució aproximad, la f(x_b)= 0.0 que vol dir que la arrel és exacta i per ultim el nombre d'interacions.

### 6. Dificultats i Solucions

- M'ha costat fer la funció de disseció, però amb la teva ajuda la he entes bastant.

### 7. Reflexió Personal

- El que era el metòde de bissecció i a millorar com s'utilitza el while.


