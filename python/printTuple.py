# Given a tuple (a, b, c)
# print
# (*,*,*)
# (*,*,c)
# (*,b,*)
# (*,b,c)
# (a,*,*)
# (a,*,c)
# (a,b,*)
# (a,b,c)

from math import pow

def printSequence(numbers):
	permutations = int(pow(2, len(numbers)))
	for i in range(0, permutations):
		chars = []
		for j in range(0, len(numbers)):
			if (i / int(pow(2, j)) % 2) == 0:
				chars.insert(0, '*')
			else:
				chars.insert(0, numbers[len(numbers) - 1 - j])

		print tuple(chars)

printSequence(('a', 'b', 'c'))
