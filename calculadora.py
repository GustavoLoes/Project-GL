print("=== CALCULADORA ===")

resultado = float(input("Digite o primeiro número: "))

while True:
    operacao = input("Digite a operação (+, -, *, / ou =): ")

    if operacao == "=":
        print("Resultado final:", resultado)
        break

    if operacao == "+":
        numero = float(input("Digite o próximo número: "))
        resultado = resultado + numero

    elif operacao == "-":
        numero = float(input("Digite o próximo número: "))
        resultado = resultado - numero

    elif operacao == "*":
        numero = float(input("Digite o próximo número: "))
        resultado = resultado * numero

    elif operacao == "/":
        numero = float(input("Digite o próximo número: "))

        if numero != 0:
            resultado = resultado / numero
        else:
            print("Erro: não é possível dividir por zero.")

    else:
        print("Operação inválida.")
