cache = {} 

def conta(n):
    if n in cache:
        return cache[n]
	
    if n <= 1:
        return 1
	
    if n % 2 == 0:
        y = n // 2
    else:
        y = 3 * n + 1
    cache[n] = conta(y) + 1
    return cache[n] 


while True:
    maximo_ciclo = 0
    try:
         x, y = map(int, input().split())
    except EOFError:
        break
    
    for i in range(min(x, y), max(x, y) + 1):
        n = conta(i)
        
        if n > maximo_ciclo:
            maximo_ciclo = n
            
    print(x, y, maximo_ciclo) 
        