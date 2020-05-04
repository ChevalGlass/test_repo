#!/usr/bin/python3.7

import re
import os

def writeFile(file, content):
	try:
		with open(file, 'w') as writeFile: # write the file.
			writeFile.write(content) # write content to file.
	except FileNotFoundError:
		os.makedirs(os.path.dirname(file)) # make all the missing directories.
		with open(file, 'w') as writeFile: # write the file.
			writeFile.write(content) # write content to file.
	except:
		print('An unexpected error occurred while trying to write a file. Exiting...')
		sys.exit(-1)


# Replace a section of a file.
def replace_between(start, end, file, repl):
	whole_file = ''
	with open(file, 'r') as open_file:
		whole_file = re.sub(r'(?<='+start+'\n)(\n*?.*?\n*?.*?)*?(?=\n'+end+'*)', repl, open_file.read())

	# "out soucrced" the write to another function with more checks in place.
	# Still could handle more error types though. Only works if the directory is writable.
	with open(file, "w") as open_file:
		open_file.write(whole_file)

# v2 with a more consice regex.
#'(?<='+start+')[\s\S]*(?='+end+')'
def replace_between2(start, end, file, repl):
	whole_file = ''
	with open(file, 'r') as open_file:
		whole_file = re.sub(r'(?<='+start+')[\\s\\S]*(?='+end+')', repl, open_file.read())

	# Save file using function with more exception catching.
	writeFile(file, whole_file)
