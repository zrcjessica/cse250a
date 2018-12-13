
# coding: utf-8

# In[14]:

import math
from numpy import random


# In[124]:

# constants
ALPHA=0.1
Z=128
N=10
SAMPLE_BITS=[2,5,8,10]


# In[125]:

def f_B(bitSeq):
    sum=0
    for i in range(len(bitSeq)):
        sum+=pow(2,i)*bitSeq[i]
    return sum


# In[126]:

def likelihood_weight(B):
    exp = abs(Z - f_B(B))
    out = ((1-ALPHA)/(1+ALPHA))*(pow(ALPHA,exp))
    return out


# In[127]:

def estimate(samples, bit):
    numer=0.0
    denom=0.0
    for i in range(samples):
        binarySeq = random.randint(2, size=N)
        pz = likelihood_weight(binarySeq)
        denom += pz
        indicator = binarySeq[bit-1]
        numer+= pz*indicator
    return numer/denom
        


# In[250]:

### 3.6b ###
print("sampling %d times" % N)
bit = 2 # {2,5,8,10}
prob = estimate(N,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 5 # {2,5,8,10}
prob = estimate(N,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 8 # {2,5,8,10}
prob = estimate(N,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 10 # {2,5,8,10}
prob = estimate(N,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))

### 3.6c ###
print("sampling %d times" % 100)
bit = 2 # {2,5,8,10}
prob = estimate(100,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 5 # {2,5,8,10}
prob = estimate(100,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 8 # {2,5,8,10}
prob = estimate(100,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 10 # {2,5,8,10}
prob = estimate(100,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))

print("sampling %d times" % 1000)
bit = 2 # {2,5,8,10}
prob = estimate(1000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 5 # {2,5,8,10}
prob = estimate(1000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 8 # {2,5,8,10}
prob = estimate(1000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 10 # {2,5,8,10}
prob = estimate(1000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))

print("sampling %d times" % 10000)
bit = 2 # {2,5,8,10}
prob = estimate(10000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 5 # {2,5,8,10}
prob = estimate(10000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 8 # {2,5,8,10}
prob = estimate(10000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 10 # {2,5,8,10}
prob = estimate(10000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))

print("sampling %d times" % 100000)
bit = 2 # {2,5,8,10}
prob = estimate(100000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 5 # {2,5,8,10}
prob = estimate(100000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 8 # {2,5,8,10}
prob = estimate(100000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 10 # {2,5,8,10}
prob = estimate(100000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))

print("sampling %d times" % 1000000)
bit = 2 # {2,5,8,10}
prob = estimate(1000000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 5 # {2,5,8,10}
prob = estimate(1000000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 8 # {2,5,8,10}
prob = estimate(1000000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))
bit = 10 # {2,5,8,10}
prob = estimate(1000000,bit)
print("P(B%d=1|Z=128) = %f" % (bit, prob))

