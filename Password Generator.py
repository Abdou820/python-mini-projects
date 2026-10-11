import os
import secrets
import string

os.system('')

GREEN_BOLD = '\033[1;92m'
RESET = '\033[0m'

def ask_length():
    while True:
        try:
            length = int(input('Enter the length of the password (minimum 8 characters): '))
            if length >= 8:
                return length
            print('Error: Password length must be at least 8 characters.')
        except ValueError:
            print('Error: Please enter a valid number for the length of the password.')

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print('Error: Please answer with "yes" or "no".')

def ask_character_types():
    while True:
        pools = []
        if ask_yes_no('Do you want capital letters? '):
            pools.append(string.ascii_uppercase)
        if ask_yes_no('Do you want lowercase letters? '):
            pools.append(string.ascii_lowercase)
        if ask_yes_no('Do you want numbers? '):
            pools.append(string.digits)
        if ask_yes_no('Do you want punctuation? '):
            pools.append(string.punctuation)

        if pools:
            return pools
        print('Error: You must select at least one character type.')

def generate_password(length, pools):
    password = [secrets.choice(pool) for pool in pools]
    all_chars = ''.join(pools)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

print('\nWELCOME TO OUR PASSWORD GENERATOR\n___________________________________\n')
length = ask_length()
pools = ask_character_types()
password = generate_password(length, pools)
print('___________________________________\n')
print('Your password is:', GREEN_BOLD + password + RESET,'\n')