from typing import List
def prueba4 (m: List[List[int]]) -> bool:
    res: bool = True
    n: int = 0
    for i in range(1, len(m)):
        for j in range(0, len(m[0])):
            n = m[1][0] - m[0][0]
            if m[i][j] - m[i-1][j] != n:
                res = False
    return res

prueba4([[2,2],[1,2]])
            