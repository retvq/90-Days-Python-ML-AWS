# NOTE This is a Simple Calculator
import math
# -----------------------
#Welcome Page
# -----------------------

print('\n'+'='* 50)
print("Welcome to Simple Calculator by Ritvik")
print('='*50)
print(f"""
Supported Operations: 
Addition(+)
Subtraction(-)
Multiplication(*)
Division(/)
Integer Division(//)
Modulo(%)
Power(**)

Format to Operate: 
1. Enter First Number, Press Enter
2. Enter Operator, Press Enter
3. Enter Second Number, Press Enter
4. Recieve Output
5. Also get History of Past Collections
""")
history = []

# Looped Operation Entry for Iterative Calculations and 'E' to exit
while True: 
    error = None
    result = None
    num1 =(input("Enter First Number or Enter (E) to Exit: ").strip()).lower()
    if num1 == 'e':
        print("Thank you for using our calculator!")
        break
    else:
        num1 = int(num1)
        opt = input("Enter Operator: ").strip()
        num2 = int(input("Enter Second Number: ").strip())

        if (opt=='+'): result = num1+num2
        elif(opt=='-'): result = num1-num2
        elif(opt=='*'): result = num1*num2
        elif(opt=='/'): 
            if(num2==0): error = "Error: Cannot Divide by Zero"
            else: result = num1/num2
        elif(opt=='//'): 
            if(num2==0): error = "Error: Cannot Divide by Zero"
            else: result = num1//num2
        elif(opt=='%'):
            if(num2==0): error = "Error: Cannot Divide by Zero"
            else: result = num1%num2
        elif(opt=='**'): 
            result = num1**num2
        else: error = f"Error: Unknown Operator '{opt}'"

        print('='*50 + "\nResult:")
        if error: print(error)
        else: 
            res = (f'{num1} {opt} {num2} = {result}')
            print(res)
            history.append(res)
            print('='* 50 + '\nHistory:')
            for f in history: print(f'{f}')

