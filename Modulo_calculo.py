def ponto():
    print("-" * 30)

operadores = ("+", "-", "/", "*")

def Calculadora():
    while True:
        try:
            num1 = float(input("Digite um valor: "))
            num2 = float(input("Digite outro valor: "))
        except ValueError:
            print("Entrada inválida, digite apenas números")
            continue

        while True:
            opr = input("Escolha um operador: ( + ) ( - ) ( / ) ( * )")
            if opr in operadores:
                break
            print("ERRO: Operador inválido, tente novamente ")

        if opr == "+":
            ponto()
            print(f"Resultado: {num1 + num2}")
            ponto()


        elif opr == "-":
            ponto()
            print(f"Resultado: {num1 - num2}")
            ponto()


        elif opr == "/":
            try:
                ponto()
                print(f"Resultado: {num1 / num2}")
                ponto()
            except ZeroDivisionError:
                print("Não é possivel dividir por 0")

        elif opr == "*":
            ponto()
            print(f"Resultado: {num1 * num2}")
            ponto()

        break