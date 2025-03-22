def generator(n):
    sq = 0
    while sq < n:
        yield sq**2
        sq += 1
    return "stop"    
n = int(input())
gen = generator(n)

for i in range (0, n):
    print(gen(generator(n)))
