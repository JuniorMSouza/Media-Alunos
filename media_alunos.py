"Exercício de Fundametação de programação em Python"
nome = input("Digite o nome completo do Aluno")

def pedir_nota():
    nota = float(input("Digite a Nota: "))

    while nota <0 or nota > 10 :
        print("Erro! Digite uma nota de 0 a 10 apenas")
        nota = float(input("Digite novamente"))

    return nota

nota1 = pedir_nota()
nota2 = pedir_nota()
nota3 = pedir_nota()
nota4 = pedir_nota()

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 6:
    resultado = "Aprovado!"
elif media >= 5:
    resultado = "de Recupereção"
else: "Reprovado"

print("O Aluno de Nome: ", nome)
print("Com Média de: ", media)
print("Está", resultado)
