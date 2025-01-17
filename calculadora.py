listaEscolhas=[]


def somar():
	num1= input("Digite o primeiro numero: ")
	num2= input("Digite o segundo numero: ")
	soma=verificarEntradasSoma(num1,num2)
	if isinstance(soma,int):
		return soma
	else:
		return 0	

def verificarEntradasSoma(num1,num2):
	try:
		primeiroNumero=int(num1)
		segundoNumero=int(num2)
		return primeiroNumero+segundoNumero
	except Exception as e:
		print("Os dois valores devem ser numericos")

	
def subtrair():
	num1= input("Digite o primeiro numero: ")
	num2= input("Digite o segundo numero: ")
	sub=verificarEntradasSubtracao(num1,num2)
	if isinstance(sub,int):
		return sub
	else:
		return 0	

def verificarEntradasSubtracao(num1,num2):
	try:
		primeiroNumero=int(num1)
		segundoNumero=int(num2)
		return primeiroNumero-segundoNumero
	except Exception as e:
		print("Os dois valores devem ser numericos")


def Multiplicar():
	num1= input("Digite o primeiro numero: ")
	num2= input("Digite o segundo numero: ")
	mult=verificarEntradasMultiplicacao(num1,num2)
	if isinstance(mult,int):
		return mult
	else:
		return 0	

def verificarEntradasMultiplicacao(num1,num2):
	try:
		primeiroNumero=int(num1)
		segundoNumero=int(num2)
		return primeiroNumero*segundoNumero
	except Exception as e:
		print("Os dois valores devem ser numericos")

	
def Dividir():
	num1= input("Digite o primeiro numero: ")
	num2= input("Digite o segundo numero: ")
	div= verificarEntradasDivisao(num1,num2)
	if isinstance(div,float):
		return div
	else:
		return 0	

def verificarEntradasDivisao(num1,num2):
	try:
		primeiroNumero=int(num1)
		segundoNumero=int(num2)
		return (primeiroNumero/segundoNumero)
	except Exception as e:
		print("Os dois valores devem ser numericos e o divisor deve ser diferente de 0.")		


def memorizarNumero():
    numeroMemorizar = input("Digite o número que deseja memorizar: ")
    try:
        # Tentativa de conversão para número
        numeroConvertido = float(numeroMemorizar) if '.' in numeroMemorizar else int(numeroMemorizar)

        # Salva o número no arquivo
        with open("memoria.txt", "a") as arquivoMemoria:
            arquivoMemoria.write(str(numeroConvertido) + "\n")
            print("Entrada salva!")
    except ValueError:
        print("Os valores memorizados só podem ser numéricos.")


print("------Calculadora------\n")

print("Digite o numero da operacao desejada ou -1 para sair:\n")
print("1-Soma.")
print("2-Subtração.")
print("3-Multiplicação. ")
print("4-Divisão. ")
print("5-Memorizar um numero. \n")

opcao=0
while (opcao != -1):
	opcao= int(input("Selecione a opção desejada: "))
	print(f'Vc selecionou a opção {opcao}')
	listaEscolhas.append(opcao)
	match (opcao):
		case 1:
			resultadoSoma= somar()
			print(f'Resultado da soma: {resultadoSoma}\n')
		case 2:
			resultadoSubtracao= subtrair()
			print(f'Resultado da subtração: {resultadoSubtracao}\n')
		case 3:
			resultadoMultiplicacao= Multiplicar()
			print(f'Resultado da multiplicação: {resultadoMultiplicacao}\n')
		case 4:
			resultadoDivisao= Dividir()
			print(f'Resultado da divisão: {resultadoDivisao}\n')
		case 5:
			memorizarNumero()
		case _:
			break
			 				
			
	


