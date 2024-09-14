
###1
i = 12
sum =0
k= 1
while(k<i):
    k=k+1
    sum += k

print(sum)


##3
faturamento_diario = [170, 235, 40, 158, 87, 0, 400, 304, 43, 250, 100, 0, 450, 501, 37, 0, 200, 300, 0, 514]

def calcular_faturamento(faturamento):
    faturamento_valido = []

    for dia in faturamento:
        if dia > 0:
            faturamento_valido.append(dia)

    if not faturamento_valido:
        return "Sem dia valido"

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_anual = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = 0
    for dia in faturamento_valido:
        if dia > media_anual:
            dias_acima_da_media += 1

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")

