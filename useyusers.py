#!/usr/bin/python3

# -*- coding: utf-8 -*-

import argparse, textwrap, re

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=textwrap.dedent('''\
	Output options:
	1\tjohn.doe
	2\tj.doe
	3\tjohndoe
	4\tjdoe
	5\tdoe.john
	6\tdoe.j
	7\tdoejohn
	8\tdjohn
	'''),epilog="Example: useyusers.py -d example.com -s 1\nOutput: john.doe@example.com\nThe cleaner your input file; the easier this will work!")
parser.add_argument("-d", "--domain", type=str, metavar="",help="Domain to append to the username")
parser.add_argument("-i", "--input", required=True, type=str, metavar="", help="The input file that useyusers will read from")
parser.add_argument("-s", "--style", required=True, type=str, metavar="", help="The variation of the username styles")
parser.add_argument("-o", "--output", metavar="", help="file to output to")
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
args = parser.parse_args()

AUTHOR="Mez0"

NAMES=args.input #reference to a file
DOMAIN=args.domain

RAW_FILE = open(NAMES, "r")#contents of the file

if args.output: #if args.output is used, open it.
	OUTPUT_FILE = open(args.output,"w")
else:
	pass

NAMES_FILE=[]

def cleanup():
	try:
		tmp = []
		lines_seen = set()

		for line in RAW_FILE:
			if len(line) > 1:
				x = re.sub(r'[!\"£$%^&*()_+-=\[\]{}#\';/.,<>?:@~]', '', line).strip().lower()
				if (len(x.split())) == 2:
					f = x.split()[0]
					s = x.split()[1]
					name = f + " " + s
					tmp.append(name)
					for new_line in tmp:
						if new_line not in lines_seen:
							NAMES_FILE.append(new_line)
							lines_seen.add(new_line)
				else:
					pass

		NAMES_FILE.sort()					
		RAW_FILE.close()

	except IndexError:
		pass						

def test():
	if args.output:
		OUTPUT_FILE.write('hello world')

def first_dot_second():
#1. first.second
	for i in NAMES_FILE:
		first = i.split(" ",1)[0].strip()
		second = i.split(" ",1)[1].strip()
		if args.domain:
			email = ("{}.{}@{}".format(first,second, DOMAIN))
			print (email)
		else:
			username = ("{}.{}".format(first,second))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username + "\n")

def f_dot_second():
#2. f.second
	for i in NAMES_FILE:
		first = i.split(" ",1)[0][0].strip()
		second = i.split(" ",1)[1].strip()
		if args.domain:
			email = ("{}.{}@{}".format(first,second, DOMAIN))
			print (email)
		else:
			username = ("{}.{}".format(first,second))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")	        

def firstsecond():
	#3. firstsecond
	for i in NAMES_FILE:
		first = i.split(" ",1)[0].strip()
		second = i.split(" ",1)[1].strip()
		if args.domain:
			email = ("{}{}@{}".format(first,second, DOMAIN))
			print (email)
		else:
			username = ("{}{}".format(first,second))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")	   	

def fsecond():
	#4. fsecond
	for i in NAMES_FILE:
		first = i.split(" ",1)[0][0].strip()
		second = i.split(" ",1)[1].strip()
		if args.domain:
			email = ("{}{}@{}".format(first,second, DOMAIN))
			print (email)
		else:
			username = ("{}{}".format(first,second))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")	  	

def second_dot_first():
	#5. second.first
	for i in NAMES_FILE:
		first = i.split(" ",1)[0].strip()
		second = i.split(" ",1)[1].strip()
		if args.domain:
			email = ("{}.{}@{}".format(second,first, DOMAIN))
			print (email)
		else:
			username = ("{}.{}".format(second,first))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")	  		

def s_dot_first():
	#6. s.first
	for i in NAMES_FILE:
		first = i.split(" ",1)[0].strip()
		second = i.split(" ",1)[1][0].strip()
		if args.domain:
			email = ("{}.{}@{}".format(second,first, DOMAIN))
			print (email)
		else:
			username = ("{}.{}".format(second,first))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")	

def secondfirst():
	#7. secondfirst
	for i in NAMES_FILE:
		first = i.split(" ",1)[0].strip()
		second = i.split(" ",1)[1].strip()
		if args.domain:
			email = ("{}{}@{}".format(second,first, DOMAIN))
			print (email)
		else:
			username = ("{}{}".format(second,first))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")	

def sfirst():
	#8. sfirst
	for i in NAMES_FILE:
		first = i.split(" ",1)[0].strip()
		second = i.split(" ",1)[1][0].strip()
		if args.domain:
			email = ("{}{}@{}".format(second,first, DOMAIN))
			print (email)
		else:
			username = ("{}{}".format(second,first))
			print (username)
		if args.output:
			OUTPUT_FILE.write(username +"\n")			

cleanup()

if args.style == "1":
	first_dot_second()

elif args.style == "2":
	f_dot_second()

elif args.style == "3":
	firstsecond()	

elif args.style == "4":
	fsecond()

elif args.style == "5":
	second_dot_first()

elif args.style == "6":
	s_dot_first()	

elif args.style == "7":
	secondfirst()

elif args.style == "8":
	sfirst()

if args.output:
	OUTPUT_FILE.close()
