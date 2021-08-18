//Calcular a média aritimética das notas de um aluno e exibir se este foi aprovado ou não.

programa
{
	
	funcao inicio()
	{
		real nota1,nota2,nota3,nota4,media
		cadeia nome,sobrenome

			escreva ("Informe o seu nome: ")
			leia (nome)
			escreva ("Informe o seu sobrenome: ")
			leia (sobrenome)
			escreva ("Informe a nota 1: ")
			leia (nota1)
			escreva ("Informe a nota 2: ")
			leia (nota2)
			escreva ("Informe a nota 3: ")
			leia (nota3)
			escreva ("Informe a nota 4: ")
			leia (nota4)
			media = (nota1+nota2+nota3+nota4)/4

				//se média >= 7 Aprovado
				se (media>=7){
					escreva ("Parabéns " + nome + " " + sobrenome + "! Sua média é " + media + " e você foi aprovado!")}
				//se média < 7 Reprovado
				senao {
					escreva ("Que pena " + nome + " " + sobrenome + "! Sua média é " + media + " e você foi reprovado!")
					
				}
						
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 721; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */