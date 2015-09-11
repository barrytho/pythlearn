
#for x in range(1,99):
#	for y in range (1,99):
#		prod = x * y 
#		if 

prod = 84566
print prod

def palin(m):
	digit = [ ]
	for txt in range(0,5):
		digit[txt] = (m / (10 ^ txt)) % (10)
#	digit[0] = (m / (1)) % 10
#	digit[1] = (m / (10)) % 10
#	digit[2] = m / (100) % 10
#	digit[3] = m / (100) % 10
	
	return digit

print palin(prod)