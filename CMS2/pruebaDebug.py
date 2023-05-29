from typing import List

def contarUnaMeseta (l: list[int]) -> int:
    meseta: int = 1
    i: int = 0
    while i < len(l) and l[i] == l[i + 1]:
        meseta = meseta + 1
        i = i + 1
            
    return meseta

x = [1,1,3,2,2]
contarUnaMeseta(x)
