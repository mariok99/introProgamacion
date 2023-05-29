from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  # definir esta función
    res: int = 0
    ruta: List[Tuple[str, str]] = []
    
    i: int = 0
    while  i < len(vuelos): # aseguro que ruta empieza con origen
        if vuelos[i][0] == origen:
            ruta = ruta + [vuelos[i]]
        i = i + 1
        
    j: int = 0
    k: int = 0
    while len(ruta) > 0 and ruta[len(ruta) - 1][1] != destino and j < len(vuelos) :
        if vuelos [j][0] != ruta[k][1]:
            j = j + 1 
        else:
            ruta = ruta + [vuelos[j]]
            del vuelos[j]
            j = 0
            k = k + 1
            
    
    if len(ruta) != 0:
        if ruta[len(ruta) - 1][1] == destino:
            res = len(ruta)
        else:
            res = - 1
    else:
        res = -1
        
    return res

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))