

def iterate(n):
	if n % 2 == 0:
		n = n / 2
	else:
		n = 3 * n + 1
	return n


def chain_length(m):
	count = 2		
	while iterate(m) <> 1:
		m = iterate (m)
		count = count + 1
	return count

list = []	
for number in range(1,1000000):
	temp = chain_length(number)
	list.append(temp)

# print list	
print max(list)
print list.index(max(list)) + 1