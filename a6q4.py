import math

f = lambda x : 4/(1+x**2)

from integrator import montecarlo
out= montecarlo(f,0,1,10000,'data1.txt')
print(f'   F_N                 sigma_f           N')
print(out)

'''
  F_N                 sigma_f           N
(3.141080650447438, 0.6441347718808105, 100000)

'''
