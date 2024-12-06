def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Menu interativo
while True:
    print("\nCalculadora no Terminal")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando...")
        break

    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos!")
        continue

    if opcao == "1":
        print(f"Resultado: {somar(n1, n2)}")
    elif opcao == "2":
        print(f"Resultado: {subtrair(n1, n2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicar(n1, n2)}")
    elif opcao == "4":
        print(f"Resultado: {dividir(n1, n2)}")
    else:
        print("Opção inválida! Escolha uma opção de 1 a 5.")
