#!/usr/bin/python

prompt = "Enter text: "
tmp_text = ""

while tmp_text != "stop":
	tmp_text = raw_input(prompt)	
	try:
		number = float(tmp_text)
		print "Number: " + str(number) + " ,third power: ", str(number ** 3)
	except ValueError:                  # kod obslugujacy bledy
		print "It isn't a number! "
