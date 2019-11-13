#!/usr/bin/python3.7

import re

# Replace a section of a file.
def replace_between(start, end, file, repl):
	whole_file = ''
	with open(file, 'r') as open_file:
		whole_file = re.sub(r'(?<='+start+'\n)(\n*?.*?\n*?.*?)*?(?=\n'+end+'*)', repl, open_file.read())

	with open(file, "w") as open_file:
		open_file.write(whole_file)
