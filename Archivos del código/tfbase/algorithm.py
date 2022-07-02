import json
from pathlib import Path
import random as r
import math
import heapq as hq
from perlin_noise import PerlinNoise


# def transformGraph():
#     n, m= 120, 60

#     noise = PerlinNoise(octaves=5, seed=1981)
#     xpix, ypix = n, m
#     pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

#     Loc= [(i * 100 - r.randint(145, 155), j * 100 - r.randint(145, 155))
#            for i in range(1, n + 1) for j in range(1, m + 1)]
#     G= [[] for _ in range(n * m)]
#     for i in range(n):
#         for j in range(m):
#             adjs= [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
#             r.shuffle(adjs)
#             for u, v in adjs:
#                 if u >= 0 and u < n and v >= 0 and v < m:
#                     G[i * m + j].append((u * m + v, pic[j][i] + 1000))
#     return G, Loc
# def bfs(G, s):
#   n= len(G)
#   visited= [False]*n
#   path= [-1]*n # parent
#   queue= [s]
#   visited[s]= True

#   while queue:
#     u= queue.pop(0)
#     for v, _ in G[u]:
#       if not visited[v]:
#         visited[v]= True
#         path[v]= u
#         queue.append(v)

#   return path

# def dfs(G, s, t):
#   n= len(G)
#   path= [-1]*n
#   visited= [False]*n

#   stack= [s]
#   while stack:
#     u= stack.pop()
#     visited[u]= True
#     if u == t:
#         break
#     for v, _ in G[u]:
#       if not visited[v]:
#         path[v]= u
#         stack.append(v)

#   return path

# def dijkstra(G, s):
#     n= len(G)
#     visited= [False]*n
#     path= [-1]*n
#     cost= [math.inf]*n

#     cost[s]= 0
#     pqueue= [(0, s)]
#     while pqueue:
#         g, u= hq.heappop(pqueue)
#         if not visited[u]:
#             visited[u]= True
#             for v, w in G[u]:
#                 if not visited[v]:
#                     f= g + w
#                     if f < cost[v]:
#                         cost[v]= f
#                         path[v]= u
#                         hq.heappush(pqueue, (f, v))

#     return path, cost



#==================================cargamos funciones==================================
# -*- coding: utf-8 -*-

import sys
print(sys.setrecursionlimit(2000))


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

import math 
import collections

def calcular_distancia(x1,y1,x2,y2):
  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 )
  return round(dist,2)

def calcular_pendiente(x1,y1,x2,y2):
  if x2 - x1 != 0:
    m = (y2 - y1) / (x2 - x1)
    is_vertical = False
  else:
    m = None
    is_vertical = True
  return is_vertical, m

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

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
def is_intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def crear_lista(arreglo):
  lista_adyacencia=[-1]*(len(arreglo))
  for i in range(len(arreglo)):
    r=[]
    for e in range(len(arreglo)):
      if e==i:
        continue
      if is_intersect([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]]):
        r.append(e)
    lista_adyacencia[i] = r
  return lista_adyacencia

def crear_lista2(arreglo):
  lista_adyacencia =[-1]*(len(arreglo))
  for i in range(len(arreglo)):
    r=[]
    for e in range(len(arreglo)):
      if e==i:
        continue
      if is_intersect([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]]):
        a, b= calcular_interseccion([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]])
        #r.append(calcular_distancia(arreglo[i][0],arreglo[i][1],a,b))
        r.append([a,b])
    lista_adyacencia[i] = r
  return lista_adyacencia

def crear_lista_calles(arreglo):
  lista_adyacencia=[-1]*(len(arreglo))
  for i in range(len(arreglo)):
    r=[]
    for e in range(len(arreglo)):
      if e==i:
        continue
      if is_intersect([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]]):
        a, b= calcular_interseccion([arreglo[i][0],arreglo[i][1]],[arreglo[i][2],arreglo[i][3]],[arreglo[e][0],arreglo[e][1]],[arreglo[e][2],arreglo[e][3]])    
        r.append((e,a,b))
        x_coordenada = [x[1] for x in r]
        y_coordenada = [x[2] for x in r]
        if ([x for x, y in collections.Counter(x_coordenada).items() if y > 1] == []):
          r_sorted = sorted(r,key = lambda value: value[1])
        elif ([x for x, y in collections.Counter(y_coordenada).items() if y > 1]) == []:
          r_sorted = sorted(r,key = lambda value: value[2])
        #r_modified = [value[0] for value in r_sorted]
    lista_adyacencia[i] = r_sorted
  return lista_adyacencia

def crear_lista_esquinas(arreglo):
  lista_adyacencia=[]
  lista_esquinas_coordenadas=[]
  for i in range(len(arreglo)):
    for e in range(len(arreglo[i])):
      temp1=[]
      if ([(i,arreglo[i][e][0])] not in lista_adyacencia) and ([(arreglo[i][e][0],i)] not in lista_adyacencia):
        temp1.append((i,arreglo[i][e][0]))
        temp2 = (arreglo[i][e][1],arreglo[i][e][2])
        #lista_adyacencia.append((i,arreglo[i][e][0]))
        lista_adyacencia.append(temp1)
        lista_esquinas_coordenadas.append(temp2)
  return lista_adyacencia, lista_esquinas_coordenadas

def modificar_lista_esquinas(esquinas, calles):
  lista_temp=esquinas[:]
  indice_der=-1
  indice_izq=-1
  for i in range(len(calles)):
    for e in range(len(calles[i])):
      if(len(calles[i])==1):
        continue
      if([(i,calles[i][e][0])] in esquinas):
        indice = esquinas.index([(i,calles[i][e][0])])
        if e == 0:
          if([(i,calles[i][e+1][0])] in esquinas):
            indice_der = esquinas.index([(i,calles[i][e+1][0])])
          if([(calles[i][e+1][0],i)] in esquinas):
            indice_der = esquinas.index([(calles[i][e+1][0],i)])
          #lista_temp[indice].append(indice_der)
          lista_temp[indice] = lista_temp[indice] + [(indice_der,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e+1][1],calles[i][e+1][2]))]
        if e>0 and e< (len(calles[i])-1):
          if([(i,calles[i][e+1][0])] in esquinas):
            indice_der = esquinas.index([(i,calles[i][e+1][0])])
          if([(calles[i][e+1][0],i)] in esquinas):
            indice_der = esquinas.index([(calles[i][e+1][0],i)])
          #lista_temp[indice].append(indice_der)
          lista_temp[indice] = lista_temp[indice] + [(indice_der,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e+1][1],calles[i][e+1][2]))]
          if([(i,calles[i][e-1][0])] in esquinas):
            indice_izq = esquinas.index([(i,calles[i][e-1][0])])
          if([(calles[i][e-1][0],i)] in esquinas):
            indice_izq = esquinas.index([(calles[i][e-1][0],i)])
          #lista_temp[indice].append(indice_izq)
          lista_temp[indice] = lista_temp[indice] + [(indice_izq,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e-1][1],calles[i][e-1][2]))]
        if e == len(calles[i])-1:
          if([(i,calles[i][e-1][0])] in esquinas):
            indice_izq = esquinas.index([(i,calles[i][e-1][0])])
          if([(calles[i][e-1][0],i)] in esquinas):
            indice_izq = esquinas.index([(calles[i][e-1][0],i)])
          #lista_temp[indice].append(indice_izq)
          lista_temp[indice] = lista_temp[indice] + [(indice_izq,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e-1][1],calles[i][e-1][2]))]
      elif([(calles[i][e][0],i)] in esquinas):
          indice = esquinas.index([(calles[i][e][0],i)])
          if e == 0:
            if([(i,calles[i][e+1][0])] in esquinas):
              indice_der = esquinas.index([(i,calles[i][e+1][0])])
            if([(calles[i][e+1][0],i)] in esquinas):
              indice_der = esquinas.index([(calles[i][e+1][0],i)])
            #lista_temp[indice].append(indice_der)
            lista_temp[indice] = lista_temp[indice] + [(indice_der,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e+1][1],calles[i][e+1][2]))]
          if e>0 and e< len(calles[i])-1:
            if([(i,calles[i][e+1][0])] in esquinas):
              indice_der = esquinas.index([(i,calles[i][e+1][0])])
            if([(calles[i][e+1][0],i)] in esquinas):
              indice_der = esquinas.index([(calles[i][e+1][0],i)])
            #lista_temp[indice].append(indice_der)
            lista_temp[indice] = lista_temp[indice] + [(indice_der,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e+1][1],calles[i][e+1][2]))]
            if([(i,calles[i][e-1][0])] in esquinas):
              indice_izq = esquinas.index([(i,calles[i][e-1][0])])
            if([(calles[i][e-1][0],i)] in esquinas):
              indice_izq = esquinas.index([(calles[i][e-1][0],i)])
            #lista_temp[indice].append(indice_izq)
            lista_temp[indice] = lista_temp[indice] + [(indice_izq,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e-1][1],calles[i][e-1][2]))]
          if e == len(calles[i])-1:
            if([(i,calles[i][e-1][0])] in esquinas):
              indice_izq = esquinas.index([(i,calles[i][e-1][0])])
            if([(calles[i][e-1][0],i)] in esquinas):
              indice_izq = esquinas.index([(calles[i][e-1][0],i)])
            #lista_temp[indice].append(indice_izq)
            lista_temp[indice] = lista_temp[indice] + [(indice_izq,calcular_distancia(calles[i][e][1],calles[i][e][2],calles[i][e-1][1],calles[i][e-1][2]))]
  lista_temp = eliminar_primero_elemento_lista(lista_temp)
  return lista_temp

def eliminar_primero_elemento_lista(arreglo):
  for i in range(len(arreglo)):
    arreglo[i].pop(0)
  return arreglo

def print_calles(arreglo):
    for i in range(len(arreglo)):
        print(f'Calle {i}: {arreglo[i]}')

def print_esquinas(arreglo):
    for i in range(len(arreglo)):
        print(f'Esquina {i}: {arreglo[i]}')

#___________

import random

# p=0
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
    if i>=tamanio:
      i=0
    _dfs2(i,arreglo,arr_arr,arr,pesos,contador,recorrido,hora_min,hora_max)
    i+=1
  return pesos

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

def corregir2(arreglo,pesos):
    tamaño=len(arreglo)
    for i in range(tamaño):
        for e in range(len(arreglo[i])):
            if not pesos[i][e]==-1:
                for j in range(len(arreglo[arreglo[i][e]])):
                    if arreglo[arreglo[i][e]][j]==i and not arreglo[arreglo[i][e]][j]==arreglo[i][e]:
                        pesos[arreglo[i][e]][j]=pesos[i][e]

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

def igualar_(trafico,distancia,max1,max2,min1,min2,pos):
    pendiente=(max1-min1)/(max2-min2)
    b=min1-(min2*pendiente)

def igualar(trafico,distancia,max1,max2,min1,min2):
    pendiente=(max1-min1)/(max2-min2)
    b=min1-(min2*pendiente)
    new_arr=trafico
    for i in range(len(trafico)):
        for e in range(len(trafico[i])):
            new_arr[i][e]=int((distancia[i][e]*pendiente)+b)
    return new_arr

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

def corregir3(distancias):
    for i in range(len(distancias)):
        for e in range(len(distancias[i])):
            if distancias[i][e]<15:
                distancias[i][e]=random.randint(15,50)
            if distancias[i][e]>500:
                distancias[i][e]=random.randint(450,500)

def unir_grafo_final(arr1, arr2):
    G=[-1]*(len(arr1))
    G_aux=[-1]*(len(arr1))
    for i in range(len(arr1)):
        aux1=[]
        aux2=[]
        for e in range(len(arr1[i])):
            aux1.append([arr1[i][e], arr2[i][e], 0])
            aux2.append((arr1[i][e], arr2[i][e]))
        G[i]=aux1
        G_aux[i]=aux2
    return G,G_aux



#___________

def crear_lista_intersecciones(lista):
  temp=[-1]*(len(lista))
  for i in range(len(lista)):
    aux=[]
    for e in range(len(lista[i])):
      aux.append(lista[i][e][0])
    temp[i]=aux
  return temp

def crear_lista_distancias(lista):
  temp=[-1]*(len(lista))
  for i in range(len(lista)):
    aux=[]
    for e in range(len(lista[i])):
      aux.append(lista[i][e][1])
    temp[i]=aux
  return temp



lista=convertir(arr_x,arr_y)
x=[]
y=[]
x1=[]
y1=[]
G=[]
#lista=crear_lista(lista)
#lista=crear_lista2(lista)
lista_calles=crear_lista_calles(lista)
#print_calles(lista_calles)
lista_esquinas, Loc=crear_lista_esquinas(lista_calles)
lista_esquinas=modificar_lista_esquinas(lista_esquinas, lista_calles)
#print_esquinas(lista_esquinas)
#print(lista_esquinas)

lista_intersecciones=crear_lista_intersecciones(lista_esquinas)
lista_distancias=crear_lista_distancias(lista_esquinas)
#print_esquinas(lista_distancias)

#Aplicar el factor de tránsito a la lista de distancias
corregir3(lista_distancias)
HORA_DEL_DIA=20
hora_min,hora_max=definir_intervalos(HORA_DEL_DIA)
aux=asignar_pesos2(lista_intersecciones,hora_min,hora_max)
corregir(aux)
arreglo=unir(aux,lista_distancias,hora_min,hora_max)
G,G_aux = unir_grafo_final(lista_intersecciones, arreglo)
#print_esquinas(G_aux)



import heapq as hq
import numpy as np
import graphviz as gv
import math

def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n

  cost[s] = 0
  pqueue = [(0, s)]
  while pqueue:
    g, u = hq.heappop(pqueue)
    if not visited[u]:
      visited[u] = True
      for v, w, l in G[u]:
        if not visited[v] and l == 0:
          f = g + w
          if f < cost[v]:
            cost[v] = f
            path[v] = u
            hq.heappush(pqueue, (f, v))

  return path, cost

def bfs_al(G, s):
  n = len(G)
  visited = [False]*n
  path1 = [-1]*n
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v, w, l in G[u]:
      if not visited[v] and l == 0:
        visited[v] = True
        path1[v] = u
        queue.append(v)

  return path1

def drawG_al(G, directed=False, weighted=False, path=[], layout="sfdp"):
  graph = gv.Digraph("felicidad") if directed else gv.Graph("alegria")
  graph.graph_attr["layout"] = layout
  graph.edge_attr["color"] = "gray"
  graph.node_attr["color"] = "orangered"
  graph.node_attr["width"] = "0.1"
  graph.node_attr["height"] = "0.1"
  graph.node_attr["fontsize"] = "8"
  graph.node_attr["fontcolor"] = "mediumslateblue"
  graph.node_attr["fontname"] = "monospace"
  graph.edge_attr["fontsize"] = "8"
  graph.edge_attr["fontname"] = "monospace"
  n = len(G)
  added = set()
  for v, u in enumerate(path):
    if u != -1:
      if weighted:
        for vi, w, f in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="orange")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  for u in range(n):
    for v, w, l in G[u]:
      draw = False
      if not directed and not f"{u},{v}" in added:  
        added.add(f"{u},{v}")
        added.add(f"{v},{u}")
        draw = True
      elif directed:
        draw = True
      if draw:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))
  return graph

def marcar_camino(inicio,fin,padre):
  padre2=[-1]*len(padre)
  aux=fin
  while fin!=inicio:
    padre2[fin]=padre[fin]
    fin=padre[fin]
  return padre2

def marcar(camino, inicio, fin):
  temp = G
  for i in range(len(G)):
    for e in range(len(G[i])):
      if temp[i][e][0]==camino[i]:
        temp[i][e][2]=1
        for k in range(len(temp[temp[i][e][0]])):
          if temp[temp[i][e][0]][k][0]==i:
            temp[temp[i][e][0]][k][2]=1
            path1 = bfs_al(temp, fin)
            if path1[inicio] != -1:
              G[i][e][2]=1
              G[G[i][e][0]][k][2]=1
            else:
              temp[i][e][2]=0
              temp[temp[i][e][0]][k][2]=0

  return

def create_path1(s,t):
  path, cost = dijkstra(G, s)
  path=marcar_camino(s,t,path)
  camino1=path
  return camino1

def create_path2(path,s,t):
  marcar(path,s,t)
  path_d, cost = dijkstra(G, s)
  path_f=marcar_camino(s,t,path_d)
  camino2=path_f
  return camino2

def create_path3(path,s,t):
  marcar(path,s,t)
  path_d, cost = dijkstra(G, s)
  path_f=marcar_camino(s,t,path_d)
  camino3=path_f
  return camino3

#print(camino1)
#print(camino2)
#print(camino3)
#==================================fin cargamos funciones==============================
# G, Loc= transformGraph()
#G=G_aux
# print(Loc)
# for i in Loc:
#   print(i)

def graph():
    return json.dumps({"loc": Loc, "g": G_aux})


def paths(s, t):
    bestpath= create_path1(s,t)
    path1= create_path2(bestpath,s,t)
    path2= create_path3(path1,s,t)

    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})
