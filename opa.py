valor = int(input("Digite um número, e terá a tabuada de 1 a 10: "))
multiplicador = 1
if valor > 0:
    for i in range(1,20):
        multiplicador = multiplicador + 1 
        resultado = valor * multiplicador
        print(f"{valor} x {multiplicador} = {resultado}")

