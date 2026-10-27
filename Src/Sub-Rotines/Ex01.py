def somar(x:int, y:int)->int:
    return x + y


def subtrair(x:int, y:int)->int:
    return x - y


# Multiplicação por sucessivas adições
def multiplicar(x:int, y:int)->int:
    resultado = 0

    for _ in range(abs(y)):
        resultado += x

    if y < 0:
        resultado = -resultado

    return resultado


# Divisão e resto por sucessivas subtrações
def dividir(dividendo:int, divisor:int)->tuple[int, int]:
    quociente = 0
    resto = dividendo

    while resto >= divisor:
        resto -= divisor
        quociente += 1

    return quociente, resto


# Potência por sucessivas multiplicações
def potencia(base:int, expoente:int)->int:
    resultado = 1

    for _ in range(expoente):
        resultado = multiplicar(resultado, base)

    return resultado


while True:
    print("\n=== CALCULADORA ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão inteira")
    print("5 - Resto da divisão")
    print("6 - Potência")
    print("0 - Sair")

    opcao = input("Escolha uma operação: ")

    if opcao == "0":
        print("Calculadora encerrada.")
        break

    if opcao == "1":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print("Resultado:", somar(numero1, numero2))

    elif opcao == "2":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print("Resultado:", subtrair(numero1, numero2))

    elif opcao == "3":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print("Resultado:", multiplicar(numero1, numero2))

    elif opcao == "4":
        numero1 = int(input("Digite o dividendo: "))
        numero2 = int(input("Digite o divisor: "))

        if numero2 == 0:
            print("Não é possível dividir por zero.")
        elif numero1 < 0 or numero2 < 0:
            print("Utilize números não negativos.")
        else:
            quociente, resto = dividir(numero1, numero2)
            print("Resultado da divisão:", quociente)

    elif opcao == "5":
        numero1 = int(input("Digite o dividendo: "))
        numero2 = int(input("Digite o divisor: "))

        if numero2 == 0:
            print("Não é possível dividir por zero.")
        elif numero1 < 0 or numero2 < 0:
            print("Utilize números não negativos.")
        else:
            quociente, resto = dividir(numero1, numero2)
            print("Resto da divisão:", resto)

    elif opcao == "6":
        numero1 = int(input("Digite a base: "))
        numero2 = int(input("Digite o expoente: "))

        if numero2 < 0:
            print("Utilize um expoente não negativo.")
        else:
            print("Resultado:", potencia(numero1, numero2))

    else:
        print("Opção inválida.")