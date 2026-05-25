import random
from math import sqrt
EPS = 0.0001

def przyst(func, l):
    return 1/(func(l)+EPS)

def get_ft(l,func):
    ft=0
    for i in l:
        ft+=func(i)
    ft/=len(l)
    return ft


def sph(l):
    ret=0
    for i in l:
        ret+= i*i
    return ret

def rosenbrock(l):
    ret=0
    for i in range(len(l)-1):
        ret += 100*(l[i+1]-l[i]*l[i])*(l[i+1]-l[i]*l[i]) + (1-l[i])*(1-l[i])
    return ret


#linear
def linear_scale(l, c,func):
    ft = get_ft(l,func)
    if min(l) > (c*ft - max(l))/(c-1):
        a = (c-1) * ft/(max(l)-ft)
        b= ft*(max(l)-c*ft)/(max(l)-ft)
    else:
        a = ft/(ft-min(l))
        b = -min(l)*a
    eval=[]
    for i in l:
        eval.append(a*func(i)+b)
    return a,b


#sigma-cut
def sig_scale(l,c,func):
    ft = get_ft(l,func)
    suma = 0
    for i in l:
        suma+=(func(i)-ft)*(func(i)-ft)
    sigma = sqrt(suma/(len(l)-1))
    eval=[]
    for i in l:
        eval.append(func(i)-ft+c*sigma)
    return eval

N=[]
for i in range(100):
    ran = random.uniform(-5.12, 5.12)
    N.append(ran)
