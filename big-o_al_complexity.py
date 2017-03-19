from math import *


# for lg n
n = 1
while log(n, 2) < 10**6:
	n += 1
	print "Minimum value of n (lg n) :", n - 1


# for sqrt n
n = 1
while sqrt(n) < 10**6:
	n += 1
	print "Minimum value of n (sqrt n) :", n - 1


# for n 
n = 1
while n < 10**6:
	n += 1
	print "Minimum value of n (n) :", n - 1


# for n lg n
n = 1
while n * log(n, 2) < 10**6:
	 n += 1
	 print "Minimum value of n (n lg n) :", n - 1


# for n**2
while pow(n,2) < 10**6:
	n += 1
	print "Minimum value of n (n**2) :", n - 1


# for n**3
while pow(n,3) < 10**6:
	n += 1
	print "Minimum value of n (n**3) :", n - 1


# for 2**n
while pow(2,n) < 10**6:
	n += 1
	print "Minimum value of n (2**n) :", n - 1


# for n!
n = 1
while factorial(n) < 10**6:
	n += 1
	print "Minimum value of n (n!)     :", n - 1
