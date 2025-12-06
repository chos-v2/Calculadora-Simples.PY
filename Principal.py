def ponto():
    print("-" * 30)
from Modulo_calculo import Calculadora
while True:

    Calculadora()

    while True:
            continuar = input("Deseja realizar um novo cálculo?: S / N").lower()
            if continuar == "n":
                print("Fim do programa")
                exit()
            elif continuar == "s":
                break
            else:
                print("Escolha S para sim ou N para não")

