def ex02():
	a = int(input('nhap canh a: '))
	b = int(input('nhap canh b: '))
	c = int(input('nhap canh c: '))
	perimeter = a + b + c
	print("chu vi = " + str(perimeter))
def ex03():
	a = int(input('nhap cd:'))
	b = int(input('nhap cr:'))

	area = a * b
	perimeter = 2*(a + b)

	print(f'chu vi = {perimeter}, dien tich = {area}')
def ex04():
	a = int(input('nhap bk:'))
	area = a*a*3,14
	perimeter = a*2*3,14

	print(f'chu vi = {perimeter}, dien tich = {area}')
def ex05():
	x = int(input('nhap x:'))
	y = 2*x-2

	print(y)
def ex06():
	import math

	x1 = int(input('nhap toa do x1: '))
	y1 = int(input('nhap toa do y1: '))
	x2 = int(input('nhap toa do x2: '))
	y2 = int(input('nhap toa do y2: '))

	m = (y2 - y1)/(x2 - x1)

	euclidean = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	print(m)
	print(euclidean)
def e07():
	pass
def e08():
	import math

	x = int(input('y = x^2 + 6x + 9 , enter x: '))
	y = x**2 + 6*x + 2

	print(f'x = {x}, y = {y}')
	delta = 6*6 - 4*2
	print(f'delta = {delta}')

	if delta < 0:
		print('pt vo nghiem')
	else:
			if delta > 0:
				x1 = (-6 + math.sqrt(delta)) / 2

				x2 = (-6 - math.sqrt(delta)) / 2

				print(f'pt co 2 nghiem {x1} va {x2}')
			else:
				x0 = -6 / 2

				print(f'pt co nghiem kep x = {x0}')
def e10():
	a = input()
	b = 'on'
	if b in a:
		print(f'"on" in {a}')
	else:
		print(f'"on" out {a}')
def e11():
	a = 'I hope this course is not full of jargon'
	b = 'jargon'
	if b in a:
		print(f'{b} in {a}')
	else:
		print(f'{b} out {a}')
def e13():
	print(len('python'))
	print(float(len('python')))
	print(str(len('python')))
def e14():
	a = int(input('enter number: '))
	if a % 2 == 0:
		print(f'{a} is even')
	else:
		print(f'{a} is odd')
def e15():
	a = int(input('enter hours: '))
	b = int(input('enter rate per hour: '))
	c == a*b

	print(f'pay = {c}')
def e16():
	b = 1 * 365 * 24 * 60 * 60
	print(f'a person can live in {b} seconds')

if __name__ == '__main__':
	ex16()
