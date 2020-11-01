import math
import random

#Midpoint method
def midpoint(f,a,b,N):
	#definining width of rectangle to be taken
	h = (b-a)/N
	M =[]
	#using loop 
	for i in range(0,N):
		#determination of mid point
		x_i = (2*a + (2*i+1)*h)/2
		#appending the areas of each rectangle fomed in a list
		M_i = (f(x_i)*h)
		M.append(M_i)
	#returning the sum area i.e. integral
	return sum(M)

#Trapezoidal method
def trapezoidal(f,a,b,N):
	#defining width
	h =(b-a)/N 

	x_0 =a
	x_N = b
	#for first and last term with weight function =1
	T=0
	T += h*(f(x_0)+f(x_N))/2
	#using loop and adding the area of trapezoid 
	for i in range(1,N):
		x_i = x_0 + i*h
		#weight function =2
		T += h*(f(x_i))
	#return total area i.e. integral	
	return T

#Simpsons Method
def simpsons(f,a,b,N):
	#width
	h= (b-a)/N
	x_0 =a
	x_N = b
	S=0
	#area under weight function =1
	S += h*(f(x_0)+f(x_N))/3 
	#looping
	for i in range(1,N):
		x_i = x_0 + i*h
		#using condition to separate even and odd terms as both have different weight functions
		if i%2 != 0:
			S += h*(4*f(x_i))/3
		if i%2 == 0:
			S += h*(2*f(x_i))/3
	#integral or total area under quadratic curves
	return S

#Error and accuracy	
def error(a,b,c,d,method):
	#using condition for each of the methods
	if method == 'simpsons':
		N = 1
		g = (b-a)**5
		j = N**4
		#establishing formulae within loop to keep the deviation within limit
		while c <= d*(g/(180*j)):
			N = N+1
			j = N**4
		return N	
	elif method == 'midpoint':
		N=1
		g = (b-a)**3
		j = N**2
		while c <= d*(g/(24*j)):
			N =N+1
			j=N**2
		return N	
	elif method == 'trapezoidal':
		N =1
		g = (b-a)**3
		j = N**2
		while c <= d*(g/(12*j)):
			N= N+1
			j=N**2
		return N	

#Monte-Carlo method		
def montecarlo(f,a,b,N,name):
 	h = (b-a)/N
 	F=[]
 	G =[]
 	#using loop and random values to get list of x
 	for i in range(0,N):
 		X_i = a+(b-a)*random.random()
 		F.append(f(X_i))
 		G.append((f(X_i))**2)
 		F_N = h*sum(F)
 		with open(name,'a') as data:
 			print(i,',',F_N,file =data)


 	#defining the sum integral function and its standard deviation	
 	F_N = h*sum(F)
 	dev = (sum(G)/N - (sum(F)/N)**2)**0.5

 	return F_N,dev,N	


