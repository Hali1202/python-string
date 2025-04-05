def ex02():
	a = int(input('enter number: '))
	if a % 2 == 0:
		print(f'{a} even')
	else:
		print(f'{a} is odd')

def ex03():
	a = int(input('enter number: '))
	if a % 7 == 0:
		print(f'{a} divisible 7')
	else:
		print(f'{a} not divisible 7')

def ex04():
	a = int(input('enter number: '))
	if a[-1] % 3 == 0:
		print('last digit of number is divisible by 3')

def ex05():
	import random

	num = random.randrange(1,10)
	print(num)

	guess_num  = input('guess the number from 1 to 9: ')

	if num == guess_num:
		print('you are true')
	else:
		print(f'wrong, the number is: {num}')

	




if __name__ == '__main__':
	ex05()


