# uma escola oferece bolsa de estudos para alunos com nota maior ou igual a 7 e frequência maior ou igual a 75%. 
# A bolsa é de 20% de desconto na mensalidade. 
# Faça um programa que leia a nota, a frequência e o valor da mensalidade do aluno e informe se ele tem direito à bolsa e o valor da mensalidade com desconto, caso tenha.


nota = float(input("nota: "))
frequencia = float(input("frequencia: "))
valor_mensalidade = float(input("digite o valor da mensalidade: ex: R$1000,00"))
bolsa = valor_mensalidade * 0.20
valor_final = valor_mensalidade - bolsa

if nota >= 7 and frequencia >= 75:
    valor_final = valor_mensalidade - bolsa
    print(f"bolsa de estudos. valor da bolsa 20%")
    print(f" valor da matricula: R$ {valor_final :.2f}")
    print(f" aluno tem direito à bolsa de R$ {bolsa :.2f}")

else:
    print("Aluno não apto para bolsa de estudos!")
     
    print(f" valor da matricula: R$ {valor_mensalidade :.2f}")
     