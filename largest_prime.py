#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import sys
import fibonnaci

def getprimenumber(number):
	fibonnaci_list = fibonnaci.fibonnaci_function(number, 0)

	prime_no = 0

	for nums in fibonnaci_list:
		count = 0

		for i in range(1, nums+1):
			if nums % i == 0:
				count += 1
			
		if count == 2:
			prime_no = nums
	
	return prime_no

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python largest_prime.py <upper_limits>")
		sys.exit(1)
	
	upper_limits = int(sys.argv[1])

	largestprimefromfib = getprimenumber(upper_limits)

	print(f"The largest prime Fibonnaci number less than {upper_limits} is: {largestprimefromfib}.")