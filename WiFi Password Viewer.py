import subprocess

data = subprocess.check_output('netsh wlan show profiles').decode(errors='ignore')

names = []
for line in data.split('\n'):
    if 'All User Profile' in line:
        names.append(line.split(':', 1)[1].strip())

for i in range(len(names)):
    print('[' + str(i + 1) + ']', names[i])

choice = int(input('\nChoose WiFi number: '))
wifi = names[choice - 1]

result = subprocess.check_output(
    'netsh wlan show profile name="' + wifi + '" key=clear').decode(errors='ignore')

password = 'not found'
for line in result.split('\n'):
    if 'Key Content' in line:
        password = line.split(':', 1)[1].strip()

print('\nNetwork:', wifi)
print('Password:', password)