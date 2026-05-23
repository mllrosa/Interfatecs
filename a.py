h_inicial, f_fracao, n_quicadas = map(float, input().split())

volta = h_inicial

for i in range(n_quicadas):
    quicada = volta * f_fracao * 2
    total = total + quicada

total = total + h_inicial
print(f"Total distance: {total}")