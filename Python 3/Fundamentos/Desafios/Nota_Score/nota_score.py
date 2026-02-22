#!/usr/bin/env python3


def main(nota):
    if nota <= 10.0 and nota >= 9.1:
        return "A"
    elif nota <= 9.0 and nota >= 8.1:
        return "A-"
    elif nota <= 8.0 and nota >= 7.1:
        return "B"
    elif nota <= 7.0 and nota >= 6.1:
        return "B-"
    elif nota <= 6.0 and nota >= 5.1:
        return "C"
    elif nota <= 5.0 and nota >= 4.1:
        return "C-"
    elif nota <= 4.0 and nota >= 3.1:
        return "D"
    elif nota <= 3.0 and nota >= 2.1:
        return "D-"
    elif nota <= 2.0 and nota >= 1.1:
        return "E"
    elif nota <= 1.0 and nota >= 0.0:
        return "E-"
    else:
        return "Nota inválida"


def score(score):
    if score == "A":
        print("O Score do aluno é: \033[34mA\033[0m")
    elif score == "A-":
        print("O Score do aluno é: \033[34mA-\033[0m")
    elif score == "B":
        print("O Score do aluno é: \033[32mB\033[0m")
    elif score == "B-":
        print("O Score do aluno é: \033[32mB-\033[0m")
    elif score == "C":
        print("O Score do aluno é: \033[33mC\033[0m")
    elif score == "C-":
        print("O Score do aluno é: \033[33mC-\033[0m")
    elif score == "D":
        print("O Score do aluno é: \033[35mD\033[0m")
    elif score == "D-":
        print("O Score do aluno é: \033[35mD-\033[0m")
    elif score == "E":
        print("O Score do aluno é: \033[31mE\033[0m")
    elif score == "E-":
        print("O Score do aluno é: \033[31mE-\033[0m")
    else:
        print("\033[33m{score}\033[0m")


if __name__ == "__main__":
    nota = float(input("Digite a nota do Aluno: "))
    nota = main(nota)
    score(nota)
