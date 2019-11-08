# exercise 3
def tripleprint(str):
	x = 1
	str2 = str
	while x < 3:
		str2 += str
		x += 1
	print(str2)

tripleprint("hello")