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




if __name__ == '__main__':
	ex06()