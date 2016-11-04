#simplifying_fractions.py
#Levi Sinclair
#11/3/16
#Simplifies fractions in the inputs array.

inputs =["4 8",
"84 6",
"1536 78360",
"51478 5536",
"46410 119340",
"7673 4729",
"4096 1024"]

def gcd(a, b):
	while b: #Python, taking inspiration from C, makes 0 values FALSE
		return gcd(b, a % b) #In the case of [0] modulo outputs 4 first because 4 % 8 = 4
	return a

def simplify(inputs):
	solved_count = 0
	while solved_count != len(inputs):
		numberwang = inputs[solved_count].split() #separates the numerator from the denomerator in an array
		numer = int(numberwang[0]) #numerator
		denom = int(numberwang[1]) #denomerator
		
		divisor = gcd(numer, denom)
		
		numer = (numer/divisor)
		denom = (denom/divisor)
		
		print "%d/%d\n" % (numer, denom)
		solved_count = solved_count + 1 #increment to grab the next fraction
	
simplify(inputs)