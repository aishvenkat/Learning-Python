from numpy import *         # so we can use the arrays
import pylab                # for plotting stuff
import re                   # regular expressions
from scipy import *
from scipy.optimize import fsolve

def linearSolve(eq1,eq2):
	""" Method for solving two linear equationsi"""
	#For Solving the Equation
	eq_pat = re.compile(r"([+-]?\d+(?:.\d+)?)\s*\*\s*\w+\s*\+\s*([+-]?\d+(?:.\d+)?)\s*\*\s*\w+\s*\=\s*([+-]?\d+(?:.\d+)?).*")
	digit_pat = re.compile(r"(\d).*")
	eq1_arr = eq_pat.findall(eq1)[0]
	eq2_arr = eq_pat.findall(eq2)[0]
	print eq1_arr
	print eq2_arr
	A = matrix([[float(eq1_arr[0]),float(eq1_arr[1])],[float(eq2_arr[0]),float(eq2_arr[1])]])
	B = matrix([[float(eq1_arr[2])],[float(eq2_arr[2])]])
	print A
	print B			
	
	C = A.I * B
	print C
	print B[0,0]	
	### To plot the graph
	# the range of x to plot
	x = linspace(0.0, 2.0, 200)
	f1 = (B[0,0] - A[0,0]*x)/A[0,1]
	pylab.plot(x,f1,'b')	
	f2 = (B[1,0] - A[1,0]*x)/A[1,1]
	pylab.plot(x,f2,'y')	
	pylab.plot(C[0],C[1],'ro')
	# label the x axis
	pylab.xlabel('x')
	# label the y axis
	pylab.ylabel('F(x)')
	# make a title
	pylab.title('Solving for intersection of two functions.')
	# show a grid in the background
	pylab.grid(True)

	# reveal the plot
	pylab.show()

#if __name__=='__main__':
#	lineareq("6*x + 4*y = -2", " -2*x + -3*y = 2.3")

	

fs11 = ""
fs12  = ""
	
def func2(x):
	""" This functions is used for solving 2 equations"""
	out = [fs11]
	out.append(fs12)
	print out
	return out

def nonlinearSolve(fs1,fs2):
	""" Method to solve 2 non linear equations """
	# function string 1
	global fs11 
	fs11 = fs1

	# function string 2
	global fs12 
	fs12 = fs2
	# reg exp to substitute for variable x in a given function string
	pattern = re.compile(r'x', re.I)

	# the range of x to plot
	x = linspace(0.0, 1.0, 200)
	start = 0.5
	
	# function based on function string 1
	f1 = eval(fs1)
	# plot it in blue
	pylab.plot(x, f1, 'b')

	# function based on function string 2
	f2 = eval(fs2)
	# plot it in yellow
	pylab.plot(x, f2, 'y')

	############ The Solving the solution part which still has problems ####	
	#soln1 = fsolve(func2,start)
	#print soln1
	#pylab.plot(soln1,func2(soln1),'ro')

	# label the x axis
	pylab.xlabel('x')
	# label the y axis
	pylab.ylabel('F(x)')
	# make a title
	pylab.title('Solving for intersection of two functions.')
	# show a grid in the background
	pylab.grid(True)

	# reveal the plot
	pylab.show()
#if __name__=='__main__':
#	nonlineareq("-x**2+1.3", "x**1.5")
