#1 calculate length of string
a = input('1. Text: ')
print('length of text: ' + str(len(a)))

#2 Count characters in string
from collections import Counter

b = input('2. Text: ')
count = Counter(b)
for char, count in count.items():
    print(f"number of {char}: " + str(count))

#3 ... in pdf
c = input('3. Text: ')

if len(c) <= 1:
	print('empty')
else:
	print(c[:2] + c[-2:])

#4 ... in pdf
d = input('4. Text: ')
first_char = d[0]
d = d[0] + d[1:].replace(first_char,'$')
print(d)

#5 ... in pdf
print('5.Text')
e = input('string 1: ')
ee = input('string 2: ')
e = ee +' '+ e
print(e)

#6 ... in pdf
f = input('6. Text: ')
 
if len(f) < 3:
	print(f)
else:
	if f[-3:] == 'ing':
		f = f + 'ly'
	else:
		f = f + 'ly'
		print(f)

#7 ... in pdf
g = input('7. Text: ')

not_index = g.find('not')
poor_index = g.find('poor')

if not_index < poor_index:
	g = g[:not_index] + 'good' + g[poor_index + 4:]
print(g)

#8 ... in pdf
h = input('8. List of words, seperated by a "space": ')
split = h.split()
longest = max(split, key=len)
print('longest word: ' + longest + "\n" + 'length: ' + str(len(longest)))

#9 ... in pdf
i = input('9. Text: ')
ii = input('Remove character index (input number): ')
remove_nth = i.replace(i[int(ii) - 1],'')
print(remove_nth)

#10 ... in pdf
j = input('10. Text: ')
swap = j[-1] + j[1:-1] + j[0]
print(swap)

#11 ... in pdf
a = input('11. Text: ')
print(a[::2])

#12 ... in pdf
b = input('12. Sentence: ')
split = b.split()
length = len(split)
print('words of sentence: ' + str(length))

#13 ... in pdf
c = input('13. Text: ')
print(a.upper())
print(a.lower())

#14 ... in pdf
d = input('14. List, seperated by a ",": ')
split = d.split()
d_sort = sorted(split)
print(d_sort)

#15 ... in pdf (don't  understand title >> skip)

#16 ... in pdf
e = input('16: String: ')
ee = input('16. String insert: ')

insert_spot = len(e) // 2

new_string = e[:insert_spot] + " " + ee + e[insert_spot:]

print(new_string)

#17 ... in pdf
f = input('17: Text: ')
f = f + f[-2:] + f[-2:] + f[-2:]
print(f)

#18 ... in pdf
g = input('18. Text: ')
if len(g) < 3:
	print(g)
else:
	print(g[0:3])

#19 ... in pdf skippp

#20 ... in pdf
h = input('20. Text: ')

if len(h) % 4 == 0:
	print(h[::-1])
else:
	print(h)

#21 ... in pdf
a = input('21. Text: ')
first_4 = a[0:4]

upper_count = sum(char.isupper() for char in first_4)

if upper_count >= 2:
	print(a.upper())
else:
	print(a)

# 22 ... in pdf
b = input('22: String: ')
sort = ''.join(sorted(b))
print(sort)