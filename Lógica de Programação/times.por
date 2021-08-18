// testar desvio condicional com várias opções
programa
{
	
	funcao inicio()
	{
		escreva("Para qual time você torce?")
		escreva(" 1 - Corinthians / 2 - São Paulo / 3 - Palmeiras / 4 - Santos \n")
		inteiro menu = 0
		escreva("\nSua escolha: ")
		leia(menu)
		escolha(menu)
		{
				caso 1: //testa se menu = 1
					escreva ("\nCorinthians\n")
				pare
		          
				caso 2: //testa se menu = 2
					escreva ("\nSão Paulo\n")
				pare
				
				caso 3: //testa se menu = 3
					escreva ("\nPalmeiras\n")
				pare
				
				caso 4: //testa se menu = 4
					escreva ("\nSantos\n")
				pare
				
				caso contrario: //opção diferente, sair do menu
					escreva ("\nSaindo do menu...\n")
		}
				
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 235; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */