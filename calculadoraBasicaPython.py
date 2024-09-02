# -*- coding: utf-8 -*-

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

def menu():
    print("Selecione a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4 ou 0 para sair): ")

        if escolha == '0':
            print("Saindo da calculadora...")
            break

        if escolha in ['1', '2', '3', '4']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {soma(a, b)}")
            elif escolha == '2':
                print(f"Resultado: {subtracao(a, b)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicacao(a, b)}")
            elif escolha == '4':
                print(f"Resultado: {divisao(a, b)}")
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()