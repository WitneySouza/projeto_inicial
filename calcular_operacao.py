def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operador inválido!"

# Receber os números e o operador do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Calcular o resultado
resultado = calcular(numero1, numero2, operador)

# Exibir o resultado
print("O resultado da operação é:", resultado)