numero = float(input("Digite um número: "))

match numero:
    case numero if numero > 0:
        print("O número é positivo.")

    case numero if numero < 0:
        print("O número é negativo.")

    case numero  if numero == 0:
        print("O número é zero.")
