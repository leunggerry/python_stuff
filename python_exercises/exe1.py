
def div7_multi5(num1, num2):
	l = []
	for i in range(num1,num2):
		if (i % 7 == 0) and (i % 5 != 0):
			l.append(str(i))
	return l

a = div7_multi5(2000, 3201)
print ','.join(a)