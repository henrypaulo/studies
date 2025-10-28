# Calculadora simples (versão sem input)
# Autor: Henrique Paulo

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    print("=== Calculadora Simples ===")
    print("Executar operações automaticamente...\n")

    a, b = 10, 5  # valores fixos de exemplo

    print(f"Soma: {a} + {b} = {soma(a, b)}")
    print(f"Subtração: {a} - {b} = {subtrai(a, b)}")
    print(f"Multiplicação: {a} × {b} = {multiplica(a, b)}")
    print(f"Divisão: {a} ÷ {b} = {divide(a, b)}")

if __name__ == "__main__":
    main()
