hora_total, brinquedos_total = map(int, input().split())
tempo_total = 60*hora_total
tempo_gasto = 0
nota_brinquedo = 0

for i in range(brinquedos_total):
    nomebrinquedo1 = input()
    nota, tempo_brincar = map(int, input().split())

    tempo_gasto = tempo_brincar + tempo_gasto
    nota_brinquedo = nota_brinquedo + nota

if tempo_gasto > tempo_total:
    print(0)
else:
    print(nota_brinquedo)
