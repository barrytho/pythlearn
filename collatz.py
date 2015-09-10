x = input("Start number ")

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
	
print chain_length(x)	