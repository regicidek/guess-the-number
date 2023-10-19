import random
n = random.randint(1,10)
print('Welcome to the game "guess the number"!')
input('if you are ready press enter')
f = int(input('enter a number from 1 to 10: '))
while n != f:
	if n < f:
		print('number is less')
	else:
		print('number is greater')
	f = int(input('please try again: '))
print('you win')
input('press enter to exit')
#w0rldk1ll
