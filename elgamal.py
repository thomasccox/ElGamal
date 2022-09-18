import random

from params import p
from params import g

def keygen():
    q = (p-1)/2
    a = random.randint(1,q)

    sk = a
    pk = pow(g,a,p)
    return pk,sk

def encrypt(pk,m):
    q = (p - 1) / 2
    r = random.randint(1, q)

    c1 = pow(g,r,p)
    c2 = (pow(pk,r,p)*m)%p
    return [c1,c2]

def decrypt(sk,c):

    h = pow(g,sk,p)

    j = pow(c[0],sk,p)
    k = pow(j,-1,p)
    m = (c[1]*k)%p
    return m
