myName = 'Alexandr'
mySurname = 'Volkov'
age = 27

print('Hello! My name is {}. Im {} years old'.format(myName, age))

opponentName = input("What is about you? What is your name?")
print('Hello, {}! Glad to see you!'.format(opponentName))

opponentAge = input('How old are you?')
opponentAge = int(opponentAge)

print('Our summary age is {}'.format(opponentAge + age))
