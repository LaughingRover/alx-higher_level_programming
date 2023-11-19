#!/usr/bin/python3
def search_replace(my_list, search, replace):
	result = []
	for val in my_list:
		if val == search:
			result.append(replace)
		else:
			result.append(val)
			
	return result
