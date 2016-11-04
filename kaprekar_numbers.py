#kaprekar_numbers.py
#Made by Levi Sinclair
#11/4/16
#Finds the kaprekar numbers in the given ranges.
#290 easy

num_range = ["1 50", "2 100", "101 9000"]

def find_kaprekars(num_range):
	count = 0
	while count < len(num_range):
		separator = num_range[count].split()

		low = int(separator[0])
		high = int(separator[1])
		
		print "The kaprekar numbers in the range of %d and %d:" % (low, high)
		
		for n in range(low, high+1): #high+1 to make it inclusive.
			squared = n * n
			s = "%d" % squared #could also just cast to str
			for i in range(1, len(s)):
				a = int(s[:i])
				b = int(s[i:])
				if(a + b == n and a != 0 and b != 0) or (n == 1):
					print n,
		print "\n"
		count = count+1

		
find_kaprekars(num_range)