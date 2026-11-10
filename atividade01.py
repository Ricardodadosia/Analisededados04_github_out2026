# Atividade 01 - Média de Notas
# Um aluno está em recuperação ou reprovado. A média mínima para aprovação é 7, para recuperação é 5 e abaixo disso é reprovado.

n1 = float(input("Digite o primeiro nota: "))
n2 = float(input("Digite o segundo nota: "))
n3 = float(input("Digite o terceiro nota: "))
n4 = float(input("Digite o quarto nota: "))

media = (n1 + n2 + n3 + n4) / 4
print(f"A média das notas é: {media}")

if media >= 7:
    print("Aluno aprovado!")    

elif media >= 5:
    print("Aluno em recuperação!")  

else:
    print("Aluno reprovado!")