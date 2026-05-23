import sys

menornum = 1
maiornum = 1000

for i in range(10):
    chute = (menornum + maiornum) // 2
    
    print(f"? {chute}")
    sys.stdout.flush()  
    
    p1 = input()
    
    if p1 == '=':
        print(f"! {chute}")
        sys.stdout.flush()
        break
    elif p1 == '<':
        maiornum = chute - 1
    elif p1 == '>':
        menornum = chute + 1
