#!/usr/bin/python3

def safe_print_integer(value):
	isInteger = False
	try:
		print("{:d}".format(value))
		isInteger = True
	except ValueError:
		isInteger = False
	finally:
		return isInteger

