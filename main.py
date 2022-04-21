import math
print('''Welcome to the simple calculator program. 
      Operations:
      Addition: "add" or "+"
      Subtraction: "subt" or "-"
      Multiplication: "mult" or "*"
      Pure Division: "div" or "/"
      Quotient & Remainder Divison: "QR" or "//"
      Exponent: "exp" or "^"
      Square Root: "sqrt" or "√"
      Factorial: "fact" or "!"''')
#Starts the infinite LookupError
while True:
  #Ask for continuing
  prompt = input('Do you wish to continue? "yes" or "no" ').lower()
  #Start the calculator if the answer is yes
  if prompt == 'yes':
    try:
      num1 = float(input('First number: '))
      oper = input('Operation: ')
      num2 = float(input('Second number: '))
      
      if oper =='add' or oper == '+':
        print(num1 + num2)
      elif oper =='sub' or oper == '-':
        print(num1 - num2)
      elif oper == 'mult' or oper == '*':
        print(num1 * num2)
      elif oper == 'div' or oper == '/':
        print(num1 / num2)
      elif oper == 'QR' or oper == '//':
        print(num1 // num2)
        print(num1 % num2)
      elif oper == 'exp' or oper == '^':
        print(num1 ^ num2)
      elif oper == 'sqrt' or oper == '√':
        print(math.sqrt(num1))
        print('Number 2 is not required')
      elif oper == 'fact' or oper == '!':
        print(math.factorial(num1))
        print('Number 2 is not required')
      else:
        print('Name a valid operation')
        continue
    except ZeroDivisionError:
      #Deals with dividing by zero
      print("Sorry, you can't divide by zero")
      continue
    except ValueError:
      #Deals with wrong datatype
      print('Please enter a valid integer or decimal.')
      continue
  elif prompt == 'no':
    break
  else:
    print('Enter a valid prompt, like yes or no')
    