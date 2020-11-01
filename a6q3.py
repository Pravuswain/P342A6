import math

f = lambda x:math.exp(-x**(2))
print(f'Method       Integral          N ')
from integrator import error
from integrator import simpsons
N1 = error(0,1,0.001,12,'simpsons')
out1= simpsons(f,0,1,N1)
print(f'simpsons:   {out1}',N1)

from integrator import error 
from integrator import midpoint
N2 = error(0,1,0.001,2,'midpoint')
out2=midpoint(f,0,1,N2)
print(f'midpoint:   {out2}',N2)

from integrator import error
from integrator import trapezoidal
N3 = error(0,1,0.001,2,'trapezoidal')
out3 = trapezoidal(f,0,1,N3)
print(f'trapezoidal:{out3}',N3)

#OUTPUT
'''
Method       Integral          N 
simpsons:   0.6921774983654256 3
midpoint:   0.7471308777479975 10
trapezoidal:0.7464612610366896 13

'''
