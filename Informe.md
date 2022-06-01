# Informe del Trabajo Final

## Introducción 

Este trabajo parcial es dirigido a los alumnos de sexto ciclo de la
carrera de Ingeniería de Software de carácter teórico-práctico, que
busca el desarrollo de la competencia general de pensamiento innovador y
la competencia específica de diseñar sistemas, componentes o procesos
para encontrar soluciones. Por el cual, se usarán todas las herramientas
aprendidas en el curso denominado Complejidad Algorítmica, donde se
generarán los grafos correspondientes. El lenguaje de programación que
se usará para conseguir el objetivo trazado es el ya enseñado por el
docente del curso, el cual tiene por denominación Python en Google
Colaboratory.

## Objetivos 

El presente trabajo parcial tiene como principal objetivo representar
una ciudad de al menos un millón de habitantes, 1500 cuadras u 800
calles en un grafo. Un grafo puede ser representado en una matriz de
adyacencia o lista de adyacencia. Nosotros optamos por representar el
grafo en una lista de adyacencia porque tiende a ser de fácil
comprensión y, además, en la impresión esta se podrá enumerar sin
problemas e imprimir de manera correcta.

## Marco conceptual 

Antes de poder cumplir o iniciar con la tarea de generar el grafo de una
ciudad es necesario escoger una ciudad que cumpla con tener al menos una
de las siguientes características: tener un millón de habitantes
aproximadamente, 1500 cuadras o 80 calles paralelas y perpendiculares
entre sí. La ciudad que optamos por escoger es Barcelona, ya que esta
cumple con todos los requisitos mencionados. Para cumplir el objetivo
general, nosotros vimos por conveniente dividir todo en subtareas.
Primero, buscamos una forma de obtener los datos de la ciudad, en la
cual, optamos por marcar calles desde Google Earth a través de la
herramienta "Agregar ruta", esta herramienta nos permite agregar puntos
en el mapa y al marcar dos puntos o más podremos ver una línea recta. Al
principio pensamos en agregar una sola ruta, de tal forma que cada punto
representaría una esquina, sin embargo, esto no era del todo eficiente
ya que tendríamos que marcar todas las esquinas por calle y esto no es
eficiente porque en una sola intersección de calles existen 4 esquinas.
Por ello, optamos por trazar puntos de inicio y final de cada calle, ya
que el número de esquinas es mayor al número de calles, entonces, cada
calle es representa por una recta. En base a esta lógica, podemos
afirmar que dos calles se cortarán entre sí y solo si hay una esquina
entre ellos. Por consecuencia, de esta forma habremos encontrado si una
calle se conecta o no con otra.

## Imagen estática de la ciudad o porción de ciudad elegida

![Mapa Descripción generada
automáticamente](./Images/image1.jpeg){width="5.905555555555556in"
height="3.334722222222222in"}\
Mapa de la ciudad de Barcelona

## Descripción de los datos consignados por calle

Cada calle tiene un punto de inicio, punto final, una zona y la
distancia de dicha calle. El punto de inicio representa el primer punto
x1 (altitud), y1 (longitud) marcado en el mapa y el punto final
representa donde termina la calle x2, y2. Con respecto a la longitud,
esta es la diferencia en metros con respecto al punto de inicio y el
punto final.

![Escala de tiempo Descripción generada
automáticamente](./Images/image2.png){width="5.905555555555556in"
height="2.216666666666667in"}

## Descripción de la información consignada por intersección

Un punto de intersección se puede representar por medio de un punto X,
Y, porque uno representa la latitud y otra la longitud. Además, una
calle se puede representar por medio de una recta, entonces, en base a
esa lógica, podemos afirmar que tendremos una intersección de calles o
una esquina cuando dos o más rectas se encuentren.

![Mapa Descripción generada
automáticamente](./Images/image3.jpeg){width="5.905555555555556in"
height="3.365972222222222in"}

## Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices

Para crear un grafo necesitamos una matriz de adyacencia o una lista de
adyacencia, nosotros optamos por una lista de adyacencia porque esta es
menos pesada que una matriz de adyacencia.

La lista de adyacencia se obtuvo a partir de las coordenadas de inicio y
fin de cada calle de la ciudad de Barcelona. Toda calle o avenida tiene
un punto de inicio y un punto final, aprovechamos esto de tal manera
que, si trazamos una recta desde el punto de inicio hacia el punto final
de una calle, obtendremos una recta. Sin embargo, este procedimiento
tiende a no ser exacto cuando las calles se tornan curvas, por ello,
optamos por marcar un punto de inicio y final que no equidisten en gran
manera. Mientras más cercanos sean estos puntos, la longitud de las
rectas será menor, y por consecuencia tendremos una mejor precisión al
buscar intersecciones. Resuelto este problema con respecto a las
longitudes e intersecciones de calles, pasamos a hacer las relaciones,
ósea que comenzamos a evaluar que calles se intersecan entre sí. Si una
calle se interseca con otra podremos afirmar que existe al menos una
esquina entre estas dos calles. La lista de adyacencia se creará a
partir de las relaciones entre calles, si una calle A se interseca con
una calle B, entonces una se agregará a la otra en la lista de
adyacencia.

Las aristas representan a una esquina y los vértices representan o nodos
representan a una calle. A continuación, mostramos una parte de la lista
de adyacencia y otra del grafo generado, además de qué en el siguiente
enlace se puede visualizar todo el grafo y lista completa:
<https://colab.research.google.com/drive/1QRikHQNLmaxyXXz1PckFvhf-7CuiAvih?usp=sharing>

![Texto Descripción generada
automáticamente](./Images/image4.png){width="5.905555555555556in"
height="3.3159722222222223in"}

![Diagrama Descripción generada
automáticamente](./Images/image5.png){width="5.905555555555556in"
height="2.459722222222222in"}
