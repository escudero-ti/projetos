# CALCULADORA EM KOTLIN
const val SOMA = 1
const val SUBTR = 2
const val MULTIP = 3
const val DIVIS = 4

fun main() {
   var operando1:Float? = 250.0f
   var operando2:Float? = 100.0f
   var res:Float?
   var operation:Int = 4

   res = calculadora(operando1, operando2, operation)
   println(res)
}

fun soma(n1:Float?, n2:Float?) = n1?.plus(n2!!)
fun subtrai(n1:Float?, n2:Float?) = n1?.minus(n2!!)
fun multiplica(n1:Float?, n2:Float?) = n1?.times(n2!!)
fun divide(n1:Float?, n2:Float?) = n1?.div(n2!!)

fun calculadora(operando1:Float?, operando2:Float?, operacaoNum:Int):Float?{
   var res:Float? = null
   var msg = ""

   if (operando1 == null || operando2 == null){
      res = null
       msg = "Um ou mais operandos é(são) nulo(s)! "
   } else {
       when {
           operacaoNum == SOMA -> {
               res = soma(operando1, operando2)
               msg = "Soma de ${operando1} e ${operando2} = "
           }
           operacaoNum == SUBTR -> {
               res = subtrai(operando1, operando2)
               msg = "Subtração de ${operando1} e ${operando2} = "
           }
           operacaoNum == MULTIP -> {
               res = multiplica(operando1, operando2)
               msg = "Multuplicação de ${operando1} e ${operando2} = "
           }
           operacaoNum == DIVIS -> {
               res = divide(operando1, operando2)
               msg = "Divisão de ${operando1} por ${operando2} = "
           }
       }
   }

   print(msg)
   return res
}
