import matplotlib.pyplot as mpl
import numpy as np
import scipy.stats  as stats

V2= [4, 3.7, 3.5, 3.3, 3.25, 3.0, 2.95] 
#V2= [3.37,2.70,2.25,1.93,1.69,1.50,1.35]
print('Recorded voltages: ',V2,'\n')

v=[]
vt= [1/V for V in V2]
for vi in vt:
    vi= round(vi,3)
    v.append(vi)
print('1/v from V: ',v,'\n')

R_v= [200,400,600,800,1000,1200,1400]
R= np.array(R_v)
print('Resistance: ',R,'\n')

m,c,r,l,err= stats.linregress(R,v)
print('slope: ',m)
print('y-intercept: ',c,'\n')

mpl.scatter(R,v,marker='.',color='red',label='Plot Points')
mpl.plot(R, (m*R)+c, color='green',label='Line of Best Fit')

mpl.plot((-c/m,200),(0,(m*200+c)),'--', color='purple',label='Extrapolation')

mpl.plot((0,0),(0,0.4))

c= round(c,3)
c2= str(c)
cl= ('y-intercept: (0, '+ c2 +')')

mpl.scatter(0,c,marker='o',color='red',label=cl)

E= 1/c
Rv= c/m
print('e.m.f= ',E,'; voltmeter resistance= ',Rv,'\n')

Vmax= []
Vmin= []

for V in V2:
    V+=0.05
    V= round(V,3)
    Vmax.append(V)
    V-=0.1
    V= round(V,3)
    Vmin.append(V)
print('minimum V: ',Vmin)
print('maximum V: ',Vmax,'\n')

vmax=[]
vmin=[]
vmaxt= [1/V for V in Vmax]
vmint= [1/V for V in Vmin]
for vi in vmaxt:
    vi= round(vi,3)
    vmax.append(vi)
for vi in vmint:
    vi= round(vi,3)
    vmin.append(vi)
print('1/v from Vmin: ',vmin)
print('1/v from Vmax: ',vmax,'\n')

mmax,cmax,r,l,err= stats.linregress(R,vmax)
mmin,cmin,r,l,err= stats.linregress(R,vmin)
print('slope from Vmax: ',round(mmax,7))
print('y-intercept from Vmax: ',round(cmax,5),'\n')
print('slope from Vmin: ',round(mmin,7))
print('y-intercept from Vmin: ',round(cmin,5),'\n')

mpl.plot(R, mmin*R+cmin,'-.',color= 'red',linewidth=1,label='minimum plot')
mpl.plot(R, mmax*R+cmax,'-.',color= 'blue',linewidth=1,label='maximum plot')
mpl.plot((R,R),(mmin*R+cmin,mmax*R+cmax),scaley= False,color='blue',linewidth=2)

dm= 0.5*(-mmax+mmin)
dc= 0.5*(-cmax+cmin)

print(cmax,cmin)

dE= E*(dc/c)
dRv= Rv*((dm/m)+(dc/c))
print('dE= ',dE,'; dRv= ',dRv,'\n')

print('Therefore; E= ,',E,'± ',dE)
print('           Rv= ,',Rv,'± ',dRv,'\n')

xin= -c/m

print('x-intercept= ',xin)
print('the x-intercept is the negative of the voltmeter resistance')

xin= round(xin,3)
xin2= str(xin)
xinl= ('x-intercept: (0, '+ xin2 +')')

mpl.scatter(xin,0.005,marker='v',color='red',label=xinl)

#mpl.errorbar(R, v, yerr=0.006, fmt='none', ecolor='b', capsize=4, label='Error Bars')

#mpl.plot(R, mmin*R+c,'r-.')
#mpl.plot(R, mmax*R+c,'b-.')
#mpl.plot((R,R),(mmin*R+c,mmax*R+c),color='blue')

mpl.title('Graph to Determine Resistance of a Voltmeter')
mpl.xlabel('Resistance, (Ω)')
mpl.ylabel('1/v, [V^ (-1)]')

mpl.xlim(-3500,1450)
mpl.ylim(0,0.37)

mpl.legend()
mpl.grid()
mpl.show()     
