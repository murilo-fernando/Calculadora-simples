def somar():
	num1= input("Digite o primeiro numero: ")
	num2= input("Digite o segundo numero: ")
	soma=verificarEntradas(num1,num2)
	if isinstance(soma,int):
		return soma
	else:
		return 0	

def verificarEntradas(num1,num2):
	try:
		primeiroNumero=int(num1)
		segundoNumero=int(num2)
		return primeiroNumero+segundoNumero
	except Exception as e:
		print("Os dois valores devem ser numericos")
	

print("------Calculadora------\n")

print("Digite o numero da operacao desejada ou -1 para sair:\n")
print("1-Soma.")
print("2-Subtração.")
print("3-Divisão. ")
print("4-Multiplicacao. \n")

opcao=0
while (opcao != -1):
	opcao= int(input("Selecione a opção desejada: "))
	print(f'Vc selecionou a opção {opcao}')
	match (opcao):
		case 1:
			result= somar()
			print(f'Resultado da soma: {result}')
		case 2:
			break
		case 3:
			break
		case 4:
			break
		case _:
			break
			 				
			
	


