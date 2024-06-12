# Iniciando o Parametro operacao com valor diferente.
operacao = None

# Definindo a função da Calculadora.
def calculadora (num1,num2,operacao):
    if operacao == 1:
        return  num1 + num2
    
    elif operacao == 2:
        return num1 - num2
    
    elif operacao == 3:
        return num1 * num2
    
    elif operacao == 4:
        return num1 / num2
    
    
# Coletando os Parametros da Calculadora:
while operacao !=0:
    operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão, 0: Sair da Calculadora): "))

    if operacao == 0:
        print("A Calculadora foi Encerrada, Até Breve!!")
        break
    elif operacao > 4:
        print("Essa opção não existe!")
        continue
    num1 = float(input("Digite o Primeiro Número: "))
    num2 = float(input("Digite o Segundo Número: "))

    # Entregando o Resultado
    resultado = calculadora(num1, num2, operacao)
    print("O Resultado é " , resultado)
