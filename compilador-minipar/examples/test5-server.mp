SEQ
  chan calculadora("localhost","localhost")
 
  string operador
  int operandoA
  int operandoB

  int resultado

  calculadora.receive(operador, operandoA, operandoB)
  
  if (operador == "+") {
    resultado = operandoA + operandoB
  }

  if (operador == "-") {
    resultado = operandoA - operandoB
  }

  if (operador == "*") {
    resultado = operandoA * operandoB
  }

  if (operador == "/") {
    resultado = operandoA / operando B
  }

  calculadora.send(resultado)

