import sys

def quienGana(j1: str, j2: str) -> str : 
    #Implementar esta funcion
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

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))