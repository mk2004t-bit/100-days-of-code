from art import calculator_art

def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def multi(n1,n2):
  return n1*n2

def div(n1,n2):
  if n2 !=0:
    return n1/n2
  else:
    return "Enter a valid input."
#Add these four functions stores in a dictonary as a values.keys are "+","-","/","*"
operations ={
  "+":add,
  "-":sub,
  "*":multi,
  "/":div,
}
def calculator():
  should_continue = True
  print(calculator_art)
  n1 = float(input("What's the first number?: "))

  while should_continue:
    for operator in operations:
      print(operator)
    operator = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
    #perform the calculations by multiply two numbers and using dictonary to trigger the functions
    output = operations[operator](n1,n2)
    print(f"{n1} {operator} {n2} = {output}")
    continue_calulation = input(f"Type 'y' to continue calculating with {output}, or Type 'n' to start a new calculation,want to stop enter \"CONTROL + C\": ").lower()
    print("\n"*10)
    if continue_calulation =="y":
        n1 = output
    else:
      should_continue = False
      calculator()

calculator()


