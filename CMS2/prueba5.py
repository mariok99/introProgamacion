from typing import List
from typing import Tuple


def borrador5 (origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
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

borrador5("A","D", [("C","D"), ("B","C"), ("A","B"),("F","E")])        

            
    
   # while vuelos != [] and ruta[len(ruta)-1] != destino:
        
        
