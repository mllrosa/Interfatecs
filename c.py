dias, duracaoCiclo= map(int, input().split())
mec = 0
for i in range(dias):
    totalciclos_diaria, tempo_refatoracao = map(int, input().split())
    mec = (duracaoCiclo * totalciclos_diaria) + tempo_refatoracao + mec

print(f"Relatorio MCE: {mec} minutos de esforço total")