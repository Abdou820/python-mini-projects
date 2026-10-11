import random

FILE_NAME = 'bot_memory.txt'

hello_words = ['hi', 'hello', 'hey']
hello_replies = ['Hello! How can I help you?', 'Hey there!', 'Hi! Nice to see you']
bye_replies = ['Goodbye!', 'See you later!', 'Bye, take care!']

def load_memory():
    memory = {}
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if ' = ' in line:
                    question, answer = line.split(' = ', 1)
                    memory[question] = answer
    except FileNotFoundError:
        pass
    return memory

def save_memory(question, answer):
    with open(FILE_NAME, 'a', encoding='utf-8') as f:
        f.write(question + ' = ' + answer + '\n')

def show_help():
    print('Commands:')
    print('  help  - show this list')
    print('  list  - show everything I learned')
    print('  bye   - exit')
    print('Or just talk to me. If I do not know the answer, you can teach me.')

def show_memory(memory):
    if len(memory) == 0:
        print('Bot: I have not learned anything yet.')
        return
    print('Bot: Here is what I know:')
    number = 1
    for question in memory:
        print(str(number) + '. ' + question + ' -> ' + memory[question])
        number += 1

def main():
    memory = load_memory()
    print('Bot: Hi! I am a small learning bot. Type help to see commands.')
    print('Bot: I know', len(memory), 'things so far.')

    while True:
        text = input('You: ').strip().lower()

        if text == '':
            continue

        if text == 'bye':
            print('Bot:', random.choice(bye_replies))
            break
        elif text == 'help':
            show_help()
        elif text == 'list':
            show_memory(memory)
        elif text in hello_words:
            print('Bot:', random.choice(hello_replies))
        elif text in memory:
            print('Bot:', memory[text])
        else:
            print('Bot: I do not know that. What should I answer?')
            answer = input('You (type skip to cancel): ').strip()
            if answer.lower() != 'skip' and answer != '':
                memory[text] = answer
                save_memory(text, answer)
                print('Bot: Thanks, I learned something new!')

main()