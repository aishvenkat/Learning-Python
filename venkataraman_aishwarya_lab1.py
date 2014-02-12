def fibonacci(n):
	""" This function return first n fibonacci numbers """
	i = 0
	j = 1
	print i,
	for p in range(n):
		print j,
		k = i + j
		i = j
		j = k

def factorial(n):
	""" The function returns factorial of n """
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

from turtle import *

def spiral(n):
	"""function to draw a spiral at point 0,0 with a starting side length n and n loops"""
	up()
	goto(0,0)
	down()
	right(90)	
	i = 1
	for j in range((n*4)-1):
		forward((j+i)*10)
		right(90)
		i = i+1


# so we don't have to wait forever"""
speed("fastest")


# when to stop window: on mouse click
exitonclick()

def branch_with_coord(n,len,x,y):
	"""function to draw an L System with 3 branches"""
	if len <= 10: 
		circle(1)
		return 0
	up()
	goto(x,y)
	down()
	left(30)
	forward(len)
#	print "Before left"
	branch_with_coord(n,(len/2),xcor(),ycor())
	up()
	goto(x,y)
	down()
	right(30)
	forward(len)
#	print "Before center"
	branch_with_coord(n,(len/2),xcor(),ycor())
	up()
	goto(x,y)
	down()
	right(30)
	forward(len)
#	print "Before right"
	branch_with_coord(n,(len/2),xcor(),ycor())


# draw L system
def branch(n,len):
	x = 0
	y = 0
	left(90)
	for k in range(n):
	#	left(90/n)
		forward(len)
		branch_with_coord(1,len/2,xcor(),ycor())
		up()
		goto(0,0)
		down()
		right(90/n)
		left(90/n)
		left(90/n)
