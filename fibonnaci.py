#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def fibonnaci_function(upper_limit, output):
    # Do something

	fibonacci = [0, 1]
	fibonacci_next = 1

	while fibonacci_next < upper_limit:
		fibonacci.append(fibonacci_next)
		fibonacci_next = fibonacci[-1] + fibonacci[-2]

	return fibonacci

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Generate Fibonacci numbers up to a limit and write them to txt file.")
	parser.add_argument("--limit", "-l", type = int, help = "The upper limit of Fibonacci number", default=True)
	parser.add_argument("--filename", "-f", help="The file to write the fibonacci numbers to", default="fibonacci_100.txt")
	args = parser.parse_args()

	try:
		fibonacci_numbers = fibonnaci_function(args.limit, args.filename)
		with open(args.filename, 'w') as file:
			file.write(str(fibonacci_numbers))
		print(f"Fibonacci numbers are found in {args.filename}")

	except IOError as e:
		print(f"An error occurred while writing to the file: {e}")