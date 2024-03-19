from art import logo

def welcome():
  print(logo)

def displayOperators():
  print("+\n-\n*\n/")

def validateNumber(prompt):
  while True:
    try:
      num = float(input(prompt))
      break
    except ValueError:
      print("You must enter a number")
  return num

def validateOperator(prompt):
  while True:
    op = input(prompt)
    if op in ["+", "-", "*", "/"]:
      break
    else:
      print("You must enter a valid operator")
      displayOperators()
  return op

def preformOperation(num1, num2, op):
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  elif op == "/":
    return num1 / num2

def displayOperatioResult(num1, num2, op, result):
  print(f"{num1} {op} {num2} = {result}")

      
def calculator():
  runningCalculation = 0
  whatIsFirstNum = "What is the first number?: "
  whatIsNextNum = "What is the next number?: "
  pickOperation = "Pick an operation: "
  continuePrompt = "Type 'y' to continue calculating with \
  {runningCalculation}, or type 'n' to exit: "
  eof = False
  welcome()
  runningCalculation = validateNumber(whatIsFirstNum)
  displayOperators()
  while not eof:
    operator = validateOperator(pickOperation)
    num2 = validateNumber(whatIsNextNum)
    total = preformOperation(runningCalculation, num2, operator)
    displayOperatioResult(runningCalculation, num2, operator, total)
    runningCalculation = total
    continueCalc = input(f"Type 'y' to continue calculating with \
    {runningCalculation}, or type 'n' to exit: ")
    if continueCalc == "n":
      eof = True
      
calculator()
print("thanks for using this calculator")

