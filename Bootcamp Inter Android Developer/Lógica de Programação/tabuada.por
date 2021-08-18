programa
{
	
	funcao inicio()
	{
		inteiro numero, limite, multiplicador
		numero=0
		limite=10

		//capaz de fazer qualquer tabuada com base no multiplicador informado pelo usuário
		escreva("Informe a tabuada desejada: ")
		leia(multiplicador)
			faca {
				escreva(multiplicador + " x " + numero + " = " + multiplicador*numero + "\n")
				numero++
			}enquanto(numero<=limite) // enquanto número for menor que limite
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 273; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */