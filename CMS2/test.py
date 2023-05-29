import borrador

borrador.gana("Piedra", "Tijera")
borrador.gana("Piedra", "Papel")
borrador.gana("Papel", "Tijera")
borrador.gana("Papel", "Piedra")
borrador.gana("Tijera", "Papel")
borrador.gana("Tijera", "Piedra")

borrador.quienGana("Piedra","Tijera") #Jugador1
borrador.quienGana("Papel","Piedra") #Jugador1
borrador.quienGana("Piedra","Piedra")  #Empate
borrador.quienGana("Tijera","Tijera")  #Empate
borrador.quienGana("Papel","Papel")  #Empate                 
borrador.quienGana("Papel","Tijera") #Jugador2
borrador.quienGana("Papel","Tijera") #Jugador2

quienGana.quienGana("Piedra","Tijera") #Jugador1
quienGana.quienGana("Papel","Piedra") #Jugador1
quienGana.quienGana("Piedra","Piedra")  #Empate
quienGana.quienGana("Tijera","Tijera")  #Empate
quienGana.quienGana("Papel","Papel")  #Empate                 
quienGana.quienGana("Papel","Tijera") #Jugador2
quienGana.quienGana("Papel","Tijera") #Jugador2

mesetaMasLarga.mesetaMasLarga([1,1,2,2,2,3])
mesetaMasLarga.mesetaMasLarga([1,1,3,3,3,3,4,4,4,4,4])
mesetaMasLarga.mesetaMasLarga([1,1,1,1,1,2,2,3,3,9])
mesetaMasLarga.mesetaMasLarga([1,1,1,2,2,3,3,9,1,1,1,1,1,1,1])

filasParecidas.filasParecidas([[1,2,3],[2,3,4],[3,4,5]])
filasParecidas.filasParecidas([[1,1,1],[1,1,1],[1,1,1]]) 
filasParecidas.filasParecidas([[1],[1],[1]]) 
filasParecidas.filasParecidas([[1,1,1],[1,1,1],[1,1,1]]) 
filasParecidas.filasParecidas([[1,3,3],[1,3,3],[1,3,3]])
filasParecidas.filasParecidas([[-1,2],[1,2],[2,4]])
filasParecidas.filasParecidas([[1,2]])  

sePuedeLlegar.sePuedeLlegar("A","B", [("H","Z"), ("B","D"), ("F","A"),("A","B")]) #res = 1
sePuedeLlegar.sePuedeLlegar("A","Z", [("H","Z"), ("E","D"), ("B","Z"),("A","B")]) #res = 2
sePuedeLlegar.sePuedeLlegar("A","D", [("C","D"), ("B","C"), ("A","B"),("F","E")]) #res = #3
sePuedeLlegar.sePuedeLlegar("A","D", []) #res = -1
sePuedeLlegar.sePuedeLlegar("A","D", [("A","D")]) #res = 1
sePuedeLlegar.sePuedeLlegar("A","D", [("A","B"), ("B","D")]) #res = 2
sePuedeLlegar.sePuedeLlegar("A","D", [("C","D")]) #res = -1
sePuedeLlegar.sePuedeLlegar("A","D", [("C","D"),("B","X")]) #res = -1
sePuedeLlegar.sePuedeLlegar("A","D", [("B","C"), ("A","B"), ("C","X")]) #res = -1
sePuedeLlegar.sePuedeLlegar("A","D", [("B","C"), ("A","B"), ("C","X"), ("X","Z"), ("Y","D"),("Z", "Y")]) #res = 6
sePuedeLlegar.sePuedeLlegar("A","D", [("B","C"), ("A","B"), ("C","X"), ("X","Z"), ("Y","D"),("Z", "Y"),("P","O"), ("O","G")]) #res = 6
sePuedeLlegar.sePuedeLlegar("A","D", [("B","C"), ("A","B"), ("C","X"), ("X","Z"), ("Y","D"),("Z", "Y"),("P","O"), ("O","G")]) #res = 6
sePuedeLlegar.sePuedeLlegar("A","Z", [("A","B"),("B","C"),("C","D"), ("D","A")]) #res = -1