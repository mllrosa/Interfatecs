n, k = map(int, input().split())


soma = 0

if n and k != 0:
    for i in range(n+1):
        soma = soma + i
    if soma % k == 0:
        if n % k == 0:
            print("POSSIVEL")
        else:
            print("IMPOSSIVEL")
    else:
        print("IMPOSSIVEL")

else:
    print("IMPOSSIVEL")