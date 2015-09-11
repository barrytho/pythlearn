n = 1
m = 2
o = 1

list = [n, m]

while m < 4000000:
	o = n + m
	n = m
	m = o
	list.append(m)

sum = 0
	
for numb in range(1,len(list)):
	if list[numb] % 2 == 0:
		sum = list[numb] + sum
		
print sum