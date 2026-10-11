print('\nWELCOME TO OUR PASSWORD STRENGTH CHECKER\n___________________________________\n')
password = input('Enter your password: ')
score = 0
has_upper = False
has_lower = False
has_number = False
has_symbol = False
if len(password) >= 8:
    score = score + 1
if len(password) >= 12:
    score = score + 1
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_number = True
    else:
        has_symbol = True
if has_upper:
    score = score + 1
if has_lower:
    score = score + 1
if has_number:
    score = score + 1
if has_symbol:
    score = score + 1
print()
print('Length:', len(password))
print('Score:', score, '/ 6')
if score <= 2:
    print('Strength: Weak')
elif score <= 4:
    print('Strength: Medium')
else:
    print('Strength: Strong')
if len(password) < 8:
    print('Tip: use at least 8 characters')
if has_upper == False:
    print('Tip: add a capital letter')
if has_lower == False:
    print('Tip: add a lowercase letter')
if has_number == False:
    print('Tip: add a number')
if has_symbol == False:
    print('Tip: add a symbol like ! or @')