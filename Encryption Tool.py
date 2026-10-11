print('\nWELCOME TO OUR ENCRYPTION TOOL\n___________________________________')

while True:
    print()
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')
    choice = input('Choose a number: ')
    if choice == '1' or choice == '2':
        text = input('Enter the text: ')
        key = int(input('Enter the key (1-25): '))
        if choice == '2':
            key = -key
        result = ''
        for char in text:
            if char.isupper():
                result = result + chr((ord(char) - 65 + key) % 26 + 65)
            elif char.islower():
                result = result + chr((ord(char) - 97 + key) % 26 + 97)
            else:
                result = result + char
        print('Result:', result)
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Wrong choice')