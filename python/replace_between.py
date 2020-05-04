#!/usr/bin/python3.7

import re

# Replace a section of a file.
def replace_between(start, end, file, repl):
	whole_file = ''
	with open(file, 'r') as open_file:
		whole_file = re.sub(r'(?<='+start+'\n)(\n*?.*?\n*?.*?)*?(?=\n'+end+'*)', repl, open_file.read())

	# This needs to protect against files that do not exist!
	with open(file, "w") as open_file:
		open_file.write(whole_file)

# v2 with a more consice regex.
#'(?<='+start+')[\s\S]*(?='+end+')'
def replace_between2(start, end, file, repl):
	whole_file = ''
	with open(file, 'r') as open_file:
		whole_file = re.sub(r'(?<='+start+')[\\s\\S]*(?='+end+')', repl, open_file.read())

	with open(file, "w") as open_file:
		open_file.write(whole_file)
