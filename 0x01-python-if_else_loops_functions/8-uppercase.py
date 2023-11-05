#!/usr/bin/python3

def uppercase(s):
	for char in s:
		if 'a' <= char <= 'z':
			# Convert lowercase characters to uppercase using ASCII code
			uppercase_char = chr(ord(char) - 32)
			print(uppercase_char, end='')
		else:
			# If the character is not lowercase, print it as is
			print(char, end='')
	print()  # Print a newline after the entire string
