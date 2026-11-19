def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if len(depositos) == 0:
        return 0.0
    else:
        return (calcular_saldo_final(depositos[:-1], tasa_interes)+ depositos[-1])*(1+tasa_interes)
print(calcular_saldo_final([1000,2000,3000], 0.05))