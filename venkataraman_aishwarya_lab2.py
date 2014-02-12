from turtle import *
import string
def graphLetterFrequency():
	""" Gives a histogram of frequency of occurences of letter in a string. Prints only the letters present in the string. Assumes that user input does not contain any special characters including period, comma etc"""
	input = raw_input("Type something here:")
	str.lower(input)
	letter_dict = dict(zip(list(string.lowercase),[0]*26))
	for i in range(len(input)):
		if str.lower(input[i]).isspace(): 
			continue
		letter_dict[str.lower(input[i])] += 1
	x = -100
	y = 0
	for j in range(26):
		if letter_dict[string.lowercase[j]] > 0:	#removing this line will give histogram for all letters
			up()
			goto(x,y)
			down()	
			write(string.lowercase[j])
			drawRect(x,y+50,10,letter_dict[string.lowercase[j]]*10)
			x = x + 20
		
def drawRect(x,y,w,h):
	""" Draws rectangle starting at co-ord(x,y) with height h and width w """
	up()
	goto(x,y)
	down()
	forward(w)
	left(90)
	forward(h)
	left(90)
	forward(w)
	left(90)
	forward(h)
	left(90)
	


# set up the drawing window
setup()

# so we don't have to wait forever"""
speed("fastest")

# when to stop window: on mouse click
exitonclick()

from math import sqrt
def stats(x):
	""" Function returns min,max,average and standard deviation of a list x of numbers"""
	minn = min(x)
	maxx = max(x)
	avg = sum(x)/len(x)
	var = 0
	for i in range(len(x)):
		var = var + ((x[i] - avg)**2)	
	stddev = sqrt(var/len(x))	
	return ([minn,maxx,avg,stddev])	
