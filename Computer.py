import time
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('Welcome to GreenOS Tree 0.0.1')
if os.name == 'nt':
 print('Running WinEdition')
else:
 print('Running LinXEdition')
print('Please wait until it downloads.')
time.sleep(3)
print('Downloaded Terminal')
time.sleep(2)
print('Downloaded input module')
time.sleep(4)
print('Downloaded GreenOS')
time.sleep(2)
print('Loaded GreenOS Tree')
print('Welcome to GreenOS Tree')
useryn = input('Do you have an acount? (Y/N) ')
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
if useryn == ('Y'):
 print('Wifi Lost! No internet!')
 print('Error 122')
 print('Creating new account...')
 user = input('What is you username? ')
 pwd = input('What is you password? ')
else:
 print('New user detected!')
 user = input('What is you username? ')
 pwd = input('What is you password? ')
time.sleep(2)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('Account done!')
print('Welcome to GreenOS Tree 0.0.1')
print('Please login:')
vuser = ('Nothing Yet!')
vpwd = ('Nothing Yet!')
while vuser != user and pwd != vpwd:
 vuser = input('Username ')
 vpwd = input('Password ')
 if vpwd != pwd and vuser != user:
  print('Wrong username and password')
 if vuser != user:
  print('Wrong username: ')
 if vpwd != pwd:
  print('Wrong password: ')
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('Welcome to GreenOS Tree 0.0.1')
print(f'Signed into {user}')
print('Now opening terminal...')
time.sleep(2)
print('Welcome to terminal')
print('Type /help for help!')
print('No need to type /, it is defaultly there.')
terminal = ('Nothing Yet!')
while terminal != ('stop'):
 terminal = input('/')
 if terminal == ('help'):
  print('Welcome to terminal help')
  if os.name == 'nt':
    print('This is the manual for WinEdition')
    print('Type /clear to clear the terminal')
    print('Type /about to see about')
  else:
     print('This is the manual for LinXEdition')
     print('Type /clear to clear the terminal')
     print('Type /about to see about')
 if terminal == ('clear'):
   if os.name == 'nt':
    os.system('cls')
   else:
    os.system('clear')
 if terminal == ('about'):
   print('Welcome to about')
   if os.name == 'nt':
     os.system('cls')
   else:
     os.system('clear')
   if os.name == 'nt':
     print('Running Green OS Tree')
     print('WinEdition')
   else:
     print('Running Green OS Tree')
     print('LinXEdition')

   print('Your username is {user}')
   pwdsee = input('Do you want to see your password? (Y/N) ')
   if pwdsee == ('Y'):
     print(f'Your password is {pwd}')
     print('About recomends you to clear your terminal.')
   if terminal == ('stop'):
     print('Shutting down...')
     time.sleep('2')
     print('Ended with a 100')
   if terminal == ('calculator'):
     print('Welcome to calculator.')
     dow = input('Do you want to use decimals? (Y/N) ')
     if dow == ('Y'):
      num = input(float('What is the first number?'))
      num2 = input(float('What is the first number?'))
      operator = input('+/-')
      if operator == ('+'):
       anwser = (num + num2)
       print(f'{num} + {num2} = ')
      if operator == ('-'):
       anwser = (num - num2)
       print(f'{num} - {num2} = ')