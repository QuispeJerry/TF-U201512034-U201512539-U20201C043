import json
import random
import math 
import numpy as np
##################################################
with open("arreglo_x.libertad") as f:
  arr_x = []#arreglo
  for line in f:
    if line == "-\n":
      arr_x.append([])
    else:
      arr_x.append([int(x) for x in line.split()])
arr_x2=[]
for i in arr_x:
  arr_x2.append(i[0])
arr_x=arr_x2
##################################################
with open("arreglo_y.libertad") as f:
  arr_y = []
  for line in f:
    if line == "-\n":
      arr_y.append([])
    else:
      arr_y.append([int(x) for x in line.split()])
arr_y2=[]
for i in arr_y:
  arr_y2.append(i[0])
arr_y=arr_y2
##################################################
def convertir(arr_x,arr_y):
    arreglo_f=[]
    i=0
    limite=(len(arr_x))
    while i<limite-1:
        p=[]
        e=i
        limitee=e+2
        while e<limitee:
            p.append(arr_x[i])
            p.append(arr_y[i])
            e+=1
            i+=1
        arreglo_f.append(p)
    return arreglo_f
##################################################
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def is_intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
##################################################
def ccw_(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0])
    
def is_intersect_(A,B,C,D):
  if ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D):
    return  ccw_(A,C,D),ccw_(A,B,C)
##################################################
def crear_lista(arreglo,x,y):
  lista_adyiaciencia=[-1]*(len(arreglo))
  for i in range(len(arreglo)):
    r=[]
    for e in range(len(arreglo)):
      continuar=False
      if e==i:
        continue
      if is_intersect([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]]):
        r.append(e)
        a,b=is_intersect_([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]])
        x.append(a)
        y.append(b)
    lista_adyiaciencia[i] = r
  return lista_adyiaciencia
##################################################
def recorrer_inversa(arreglo,recorrido,hora_min,hora_max):
  if hora_min>=10 and hora_max<=20:
    a=random.randint(10,20)
    b=random.randint(10,20)
  elif hora_min>=20 and hora_max<=30:
    a=random.randint(20,30)
    b=random.randint(20,30)
  elif hora_min>=30 and hora_max<=40:
    a=random.randint(30,40)
    b=random.randint(30,40)
  else:
    a=random.randint(40,50)
    b=random.randint(40,50)
  tamanio=len(recorrido)
  if a<b:
    y1=a
    y2=b
  else:
    y2=a
    y1=b
  x1=0
  x2=tamanio
  denominador=x2-x1
  m=(y2-y1)/denominador
  b=y1
  resultados=[-20]*tamanio
  for i in range(tamanio):
    resultados[i]=(i*m)+b
    if resultados[i]==-1:
      print("menos")
  for i in range(tamanio):
    arreglo[recorrido[i][0]][recorrido[i][1]]=int(resultados[i])
##################################################
def asignar_pesos2(arreglo,hora_min,hora_max):
  tamanio=len(arreglo)
  arr=[False]*tamanio
  arr_arr=[False]*tamanio
  pesos=[-1]*tamanio
  for i in range(tamanio):
    arr_arr[i]=[False]*len(arreglo[i])
    pesos[i]=[-1]*len(arreglo[i])
  contador=[0]
  recorrido=[]
  
  i=0
  while False in arr:
    if i>tamanio:
      i=0
    _dfs2(i,arreglo,arr_arr,arr,pesos,contador,recorrido,hora_min,hora_max)
    i+=1
  return pesos
##################################################
def _dfs2(u,arreglo,arr_arr,arr,pesos,contador,recorrido,hora_min,hora_max):
  marcador=True
  for i in arr_arr[u]:
    if not i:
      marcador=False
      break
  if marcador:
    arr[u]=True
  for v in range(len(arreglo[u])):
    if arr_arr[u][v]==False:
        arr_arr[u][v] = True
        recorrido.append([u,v])
        for k in range(len(arreglo[arreglo[u][v]])):
          if arreglo[arreglo[u][v]][k]==u and arr_arr[arreglo[u][v]][k]==False:
            arr_arr[arreglo[u][v]][k]=True
            recorrido.append([int(arreglo[u][v]),k])
        if contador[0]==25:
          contador[0]=0
          recorrer_inversa(pesos,recorrido,hora_min,hora_max)
          recorrido=[]
        contador[0]+=1
        _dfs2(arreglo[u][v],arreglo,arr_arr,arr,pesos,contador,recorrido,hora_min,hora_max)
##################################################
def buscar_vacios(arreglo):
    contador=0
    for i in range(len(arreglo)):
        for e in range(len(arreglo[i])):
            if -1==arreglo[i][e]:
                contador+=1
    print(f'existen {contador} vacios')
##################################################
def corregir2(arreglo,pesos):
    tamaño=len(arreglo)
    for i in range(tamaño):
        for e in range(len(arreglo[i])):
            if not pesos[i][e]==-1:
                for j in range(len(arreglo[arreglo[i][e]])):
                    if arreglo[arreglo[i][e]][j]==i and not arreglo[arreglo[i][e]][j]==arreglo[i][e]:
                        pesos[arreglo[i][e]][j]=pesos[i][e]
##################################################
def calcular_distancia(x1,y1,x2,y2):
  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 )
  return round(dist,2)
##################################################
def calcular_pendiente(x1,y1,x2,y2):
  if x2 - x1 != 0:
    m = (y2 - y1) / (x2 - x1)
    is_vertical = False
  else:
    m = None
    is_vertical = True
  return is_vertical, m
##################################################
def calcular_interseccion(i1,f1,i2,f2):
  f1, m1 = calcular_pendiente(i1[0],i1[1],f1[0],f1[1])
  f2, m2 = calcular_pendiente(i2[0],i2[1],f2[0],f2[1])
  if(m1 is not None and m2 is not None):
    coord_x=(i2[1]-i1[1]-(m2*i2[0])+(m1*i1[0]))/(m1-m2)
    coord_y=(i2[0]-i1[0]-(i2[1]/m2)+(i1[1]/m1))/((1/m1)-(1/m2))
  elif f1 and ~f2:
    coord_x=i1[0]
    coord_y=m2*(i1[0]-i2[0])+i2[1]
  elif f2 and ~f1:
    coord_x=i2[0]
    coord_y=m1*(i2[0]-i1[0])+i1[1]
  return round(coord_x,2),round(coord_y,2)
##################################################
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
def is_intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
##################################################
def crear_lista2(arreglo,x,y):
  lista_adyiaciencia=[-1]*(len(arreglo))
  for i in range(len(arreglo)):
    r=[]
    for e in range(len(arreglo)):
      continuar=False
      if e==i:
        continue
      if is_intersect([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]]):
        a, b= calcular_interseccion([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]])
        x.append(a)
        y.append(b)
        r.append(calcular_distancia(arreglo[i][0],arreglo[i][1],a,b))
    lista_adyiaciencia[i] = r
  return lista_adyiaciencia
##################################################
def corregir(pesos):
    for i in range(len(pesos)):
        suma=0
        cont=0
        resultado=0
        if -1 in pesos[i]:
            for e in range(len(pesos[i])):
                if not pesos[i][e]==-1:
                    suma+=(pesos[i][e])
                    cont+=1
            if resultado<0 or cont==0:
                resultado=1
            else:
                resultado=(suma/cont)
            for k in range(len(pesos[i])):
                if pesos[i][k]==-1:
                    pesos[i][k]=int(resultado)
##################################################
def igualar_(trafico,distancia,max1,max2,min1,min2,pos):
    pendiente=(max1-min1)/(max2-min2)
    b=min1-(min2*pendiente)
##################################################
def igualar(trafico,distancia,max1,max2,min1,min2):
    pendiente=(max1-min1)/(max2-min2)
    b=min1-(min2*pendiente)
    new_arr=trafico
    for i in range(len(trafico)):
        for e in range(len(trafico[i])):
            new_arr[i][e]=int((distancia[i][e]*pendiente)+b)
    return new_arr
##################################################
def print_pesos(arreglo):
    for i in range(len(arreglo)):
        print(f'calle {i}: {arreglo[i]}')
##################################################
def unir(trafico,distancia,hora_min,hora_max):
    lim_trafico=hora_max
    min_trafico=hora_min
    lim_distancia=500
    min_distancia=30
    distancia_=igualar(trafico,distancia,lim_trafico,lim_distancia,min_trafico,min_distancia)
    new_arr=distancia_
    for i in range(len(distancia_)):
        for e in range(len(trafico[i])):
            new_arr[i][e]=int((distancia_[i][e]+trafico[i][e])/2)
    return new_arr
##################################################
def definir_intervalos(hora):
    hora_max=-1
    hora_min=-1
    if hora>=0 and hora<=4:#0
        hora_max=25
        hora_min=0
    elif hora>=21 and hora<=24:#1
        hora_max=50
        hora_min=26
    elif (hora>=9 and hora<=11) or (hora>=15 and hora<=17):#2
        hora_max=75
        hora_min=51
    elif (hora>=4 and hora<=9) or (hora>=11 and hora<=15) or (hora>=17 and hora<=21):#3
        hora_max=100
        hora_min=76
    return hora_min,hora_max
##################################################
def corregir3(distancias):
    for i in range(len(distancias)):
        for e in range(len(distancias[i])):
            if distancias[i][e]<15:
                distancias[i][e]=random.randint(15,50)
            if distancias[i][e]>500:
                distancias[i][e]=random.randint(450,500)
##################################################
def unir_grafo_final(arr1, arr2):
    G=[-1]*(len(arr1))
    for i in range(len(arr1)):
        aux = []
        for e in range(len(arr1[i])):
            aux.append([arr1[i][e], arr2[i][e], 0])
        G[i]=aux
    return G
##################################################
lista=convertir(arr_x,arr_y)
x=[]
y=[]

lista=crear_lista(lista,x,y)
# print_pesos(lista)
##################################################

def graph():
    Loc = [(10, 10), (10, 24), (23, 22), (22, 11)]
    G = [[(1, 2), (3, 1)],
         [(2, 3)],
         [(3, 3)],
         []]

    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    bestpath = [-1, 0, 1, 0]
    path1 = [-1, 0, 1, 0]
    path2 = [-1, 0, 1, 0]

    # bestpath = []
    # path1 = []
    # path2 = []



    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)

