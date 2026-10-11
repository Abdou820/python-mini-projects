print('\nWELCOME TO YOUR PASSWORD MANAGER')

while True:
    print()
    print('1. Add password')
    print('2. Show all passwords')
    print('3. Search by site')
    print('4. Exit')
    choice = input('Choose a number: ')
    if choice == '1':
        site = input('Site name: ')
        username = input('Username: ')
        password = input('Password: ')
        file = open('passwords.txt', 'a')
        file.write(site + ' | ' + username + ' | ' + password + '\n')
        file.close()
        print('Saved!')
    elif choice == '2':
        try:
            file = open('passwords.txt', 'r')
            lines = file.readlines()
            file.close()
            if len(lines) == 0:
                print('No passwords yet')
            else:
                for line in lines:
                    parts = line.strip().split(' | ')
                    print('Site:', parts[0])
                    print('Username:', parts[1])
                    print('Password:', parts[2])
                    print('-----------')
        except FileNotFoundError:
            print('No passwords yet')
    elif choice == '3':
        name = input('Site to search: ')
        found = False
        try:
            file = open('passwords.txt', 'r')
            lines = file.readlines()
            file.close()
            for line in lines:
                parts = line.strip().split(' | ')
                if parts[0].lower() == name.lower():
                    print('Username:', parts[1])
                    print('Password:', parts[2])
                    found = True
            if found == False:
                print('Site not found')
        except FileNotFoundError:
            print('No passwords yet')
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Wrong choice')