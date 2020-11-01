
f = lambda x: x/(1 + x)

from integrator import midpoint

out1 = midpoint(f,1,3,5)
out2 =midpoint(f,1,3,10)
out3 =midpoint(f,1,3,25)

print(f'Midpoint method :')
print(f'#5 :{out1}')
print(f'#10 :{out2}')
print(f'#25 :{out3}')

from integrator import trapezoidal

out4 = trapezoidal(f,1,3,5)
out5 = trapezoidal(f,1,3,10)
out6 = trapezoidal(f,1,3,25)
print(f'Trapezoidal method : ')
print(f'#5 :{out4}')
print(f'#10 :{out5}')
print(f'#25 :{out6}')

from integrator import simpsons

out7 = simpsons(f,1,3,4)
out8 = simpsons(f,1,3,10)
out9 = simpsons(f,1,3,24)


print(f'Simpsons method :')
print(f'#5 :{out7}')
print(f'#10 :{out8}')
print(f'#25 :{out9}')

#OUTPUT
'''
Midpoint method :
#5 :1.308092114284065
#10 :1.3071646395900398
#25 :1.3069028019555275
Trapezoidal method :
#5 :1.3043650793650794
#10 :1.306228596824572
#25 :1.306752839424082
Simpsons method :
#5 :1.3067460317460318
#10 :1.3068497693110697
#25 :1.306852725655682

'''