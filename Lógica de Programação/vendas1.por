programa
{
	
	funcao inicio()
	{
		real janeiro,fevereiro,marco,abril,media
		cadeia vendedor

			escreva("Informe o nome do vendedor: ")
			leia (vendedor)
			escreva("Informe o valor da venda de Janeiro 1: R$ ")
			leia (janeiro)
			escreva("Informe o valor da venda de Fevereiro: R$ ")
			leia (fevereiro)
			escreva("Informe o valor da venda de Março: R$ ")
			leia (marco)
			escreva("Informe o valor da venda de Abril: R$ ")
			leia (abril)

			media = (janeiro+fevereiro+marco+abril)/4

			escreva ("Olá " + vendedor + ". Seu total de vendas no período foi R$ " + (janeiro+fevereiro+marco+abril) + " e sua média R$ " + media)
			
	}
}


/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 428; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */