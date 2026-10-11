print('\nWELCOME TO YOUR TO DO LIST\n___________________________________\n')

tasks = []

while True:
    print()
    print('1. Add task')
    print('2. Show tasks')
    print('3. Delete task')
    print('4. Exit')
    choice = input('Choose a number: ')
    if choice == '1':
        task = input('Enter the task: ')
        tasks.append(task)
        print('\n___________________________________\nTask added!')
    elif choice == '2':
        if len(tasks) == 0:
            print('\n___________________________________\nNo tasks yet')
        else:
            for i in range(len(tasks)):
                print('\n',str(i + 1) + '. ' + tasks[i])
    elif choice == '3':
        if len(tasks) == 0:
            print('\n___________________________________\nNo tasks to delete')
        else:
            for i in range(len(tasks)):
                print('\n',str(i + 1) + '. ' + tasks[i])
            num = int(input('Which task number to delete? '))
            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print('\n___________________________________\nTask deleted!')
            else:
                print('Wrong number')
    elif choice == '4':
        print('\n___________________________________\nGoodbye!\n')
        break
    else:
        print('Wrong choice')