from typing import List

def contarUnaMeseta (l: list[int]) -> int:
    meseta: int = 1
    i: int = 0
    if len(l) > 0:
        while i < (len(l) - 1) and l[i] == l[i + 1]:
            meseta = meseta + 1
            i = i + 1
    else:
        meseta = 0
            
    return meseta
            
def borrarNVeces(l: list[int], n: int): #borra empezando desde el primer elemento 
    res = []
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

def borradorEj3 (l: List[int]) -> int:
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

borradorEj3([1,1,2,2,2,3])



