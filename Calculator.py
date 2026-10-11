print('\nWELCOME TO OUR CALCULATOR\n___________________________________\n')

while True:
    num1 = float(input('First number: '))
    op = input('Operation (+, -, *, /): ')
    num2 = float(input('Second number: '))
    if op == '+':
        print('Result:', num1 + num2)
    elif op == '-':
        print('Result:', num1 - num2)
    elif op == '*':
        print('Result:', num1 * num2)
    elif op == '/':
        if num2 == 0:
            print('Error: cannot divide by zero')
        else:
            print('Result:', num1 / num2)
    else:
        print('Error: wrong operation')
    again = input('Do you want to calculate again? (y/n): ')
    if again == 'n':
        break