#!/usr/bin/python
#print "hello"
import math
def primes(n):
	"return a sorted list of prime numbers less equal than n"
	flag = []
	for i in range(n + 1):
		flag.append(True)
	upper = math.sqrt(n)
	for i in range(2, int(math.ceil(upper))):
		if flag[i]:
			j = i
			while i * j <= n:
				flag[i * j] = False
				j = j + 1		
	L = []
	for i in range(2, n + 1):
		if flag[i] == True:
			L.append(i)
	return L

def sumOfPrimes(k):
	"return two primes a and b such that a + b = k or 0 if no such primes exists"
	L = primes(k)
	for i in L:
		if k-i in L:
			return (i, k-i)
		else:
			continue			
	return 0

def allSumOfPrimes(k):
	"returns a list of all pairs (a,b) such that a and b are prime, a + b = k"
	L = primes(k)
	LI = []
	for i in L:
		if (k-i in L) and i <= k - i:
			LI.append((i, k-i))			
	if len(LI) == 0:
		return 0
	else:
		return LI

def goldbach(k):
	"return a list of all the even numbers less equal than k being added by 2 primes"
	L = primes(k)
	LIS = []
	f = []
	c = 0
	for i in range(k + 1):
		f.append(False)
	for i in range(4, k + 1, 2):
		for j in L:
			if i-j in L and not f[i]:
				LIS.append((i, j, i-j))
				f[i] = True
				c = c + 1
	if c == 1 + int(k-4)/2:
		return(LIS, True)
	else:
		return(LIS, False)

def goldbachWidth(k):
	#returns a dictionary (map) D such that D[z] is the number of ways 
	#each even number 2 < z <= k can be written as the sum of two primes
	L = primes(k)
	D = dict()
	C = []
	for i in range (k + 1):
		C.append(0)
	for i in range(4, k + 1, 2):
		for j in L:
			if i-j in L and j <= i-j:
				C[i] = C[i] + 1
		D[i] = C[i]
	return D

def main():
	print primes(100)
	print sumOfPrimes(28)
	print allSumOfPrimes(48)
	print goldbach(12)
	print goldbachWidth(25)
if __name__ == "__main__": main() # call main if program run from command line