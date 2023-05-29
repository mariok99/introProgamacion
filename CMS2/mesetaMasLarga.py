from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  # Implementar esta funcion
    meseta1: int = 1
    meseta2: int = 1
    mesetaMayor: int = 0
    copia: List[int] = []
    copia = copia + l 
    valoresMesetas: List[int] = []
    if len(l) > 0:
        while len(copia) > 0:
            meseta1 = contarUnaMeseta(copia)
            meseta2 = contarUnaMeseta (borrarNVeces(copia, meseta1))
            valoresMesetas = valoresMesetas + [mayor(meseta1, meseta2)]
            copia = borrarNVeces(copia, meseta1)
        mesetaMayor = max(valoresMesetas)
    else:
        mesetaMayor
      
    return mesetaMayor
  
def contarUnaMeseta (l: List[int]) -> int:
    meseta: int = 1
    i: int = 0
    if len(l) > 0:
        while i < (len(l) - 1) and l[i] == l[i + 1]:
            meseta = meseta + 1
            i = i + 1
    else:
        meseta = 0
            
    return meseta
            
def borrarNVeces(l: List[int], n: int) -> List[int]: #borra empezando desde el primer elemento 
    res: List[int] = []
    for i in range(0, len(l)): #entre 0 y n-1 hay n numeros
        if i >= n:
            res = res + [l[i]]
    return res

def mayor(n1: int, n2: int) -> int:
    res: int = 0
    if n1 >= n2:
        res = n1
    else:
        res = n2
    return res

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))