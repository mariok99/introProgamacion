from typing import List

def quienGana(j1: str, j2: str) -> str : 
    res: str = ""
    ganaJ1: bool = gana(j1, j2)
    ganaJ2: bool = gana(j2, j1)
    
    if ganaJ1 == True:
        res = "Jugador1"
    
    if ganaJ2 == True:
        res = "Jugador2"
        
    if not ganaJ1 and not ganaJ2:
        res = "Empate"
        
    return res

def gana(j1: str, j2: str) -> bool: # Verdadero si el primer jugador gana #
    res = False
    if (j1 == "Piedra" and j2 == "Tijera"):
        res =  True
    if (j1 == "Tijera" and j2 == "Papel"):
        res =  True
    if (j1 == "Papel" and j2 == "Piedra"):
        res =  True
    return res

# FibonacciNoRecursivo "borrador"

def borradorEj2 (n: int) -> int:
    res: int = 0
    seqFibonacci: list[int] = []
    for i in range(0, n + 1):
        if i == 0:
            seqFibonacci = seqFibonacci + [0]
        if i == 1:
            seqFibonacci = seqFibonacci + [1]
        if i >= 2:
            seqFibonacci = seqFibonacci + [seqFibonacci[i-1] + seqFibonacci[i-2]]
    print("secuencia es: ", seqFibonacci)
    longitud: int = len(seqFibonacci)
    print ("longitud = ", longitud )   
    res = seqFibonacci[longitud - 1]
    return res

# borrador de mesetaMasLarga
def borradorEj3 (l: List[int]) -> int:
    meseta1: int = 1
    meseta2: int = 1
    copia: list[int] = []
    copia = copia + l 
    mayorEntre1y2: int = 0
    if len(l) > 0:
        while len(copia) > 0:
            meseta1 = contarUnaMeseta(copia)
            meseta2 = contarUnaMeseta (borrarNVeces(copia, meseta1))
            mayorEntre1y2: int = mayor(meseta1, meseta2)
            meseta1 = mayorEntre1y2
            copia = borrarNVeces(copia, meseta1)
        
    else:
        meseta1 = 0
        
    return meseta1



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
            
def borrarNVeces(l: list[int], n: int): #borra empezando desde el primer elemento, cambia referencia de l. 
    res = []
    for i in range(0, len(l)): #entre 0 y n-1 hay n numeros
        if i >= n:
            res = res + [l[i]]
    l = res
    print ("deberia haber cambiado", l)

def mayor(n1: int, n2: int) -> int:
    res: int = 0
    if n1 >= n2:
        res = n1
    else:
        res = n2
    return res

borradorEj3([1,1,2,2,2,3])
    
        