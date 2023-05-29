import sys

def fibonacciNoRecursivo(n: int) -> int:
    res: int = 0
    seqFibonacci: list[int] = []
    
    for i in range(0, n + 1):
        if i == 0:
            seqFibonacci = seqFibonacci + [0]
        if i == 1:
            seqFibonacci = seqFibonacci + [1]
        if i >= 2:
            seqFibonacci = seqFibonacci + [seqFibonacci[i-1] + seqFibonacci[i-2]]
            
    longitud: int = len(seqFibonacci)
    res = seqFibonacci[longitud - 1]
    
    return res  
  


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))