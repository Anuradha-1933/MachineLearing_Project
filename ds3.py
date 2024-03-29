# -*- coding: utf-8 -*-
"""DS3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13GBt4J0NhQ6rAkri_m6ACL1KCc4S4pZo
"""

import numpy as np

"""empty array as well as full array

"""

np.empty((5,2))

np.full((5,2),0)

np.diag([1,2,3])

np.diag([1,2,3,4])

np.ones(100)

np.ones(100,dtype='int64').shape

np.ones(100,dtype='int64')

np.full((100,),1)

np.eye(4)

np.eye(4,dtype='int64')

np.linspace(0,64)

np.linspace(0,64).shape

np.linspace(0,64,9)

np.zeros((2,3),dtype='int64')

"""any vs all"""

a=np.array([1,2,3,0])

a

np.any(a==0)

np.any(a==4)

np.all(a==0)

"""Trigonometric function"""

angle=np.array([0,np.pi/2,np.pi])
angle

np.sin(angle)

np.cos(angle)

"""exponential and log function"""

b=np.array([0,1])

np.exp(b)

np.log(b)

b

b[1]

b[-1]

b[-2]



random_array=np.random.rand(4,4)

"""random number choose between the range in 0 to 1(if range is not defined) means by default it takes range between 0 to 1


"""

random_array

x2=np.random.randint(10,size=(4,3)) #range values takes between 0 to 9

x2

x2[0][2]

x2[-1]

x2[-1][1]

x=np.arange(-5,1)

x

"""boolean masks"""

a=np.arange(-3,5)

a

a>0

a[a>0] #mask as a filter to get positive number

a=np.loadtxt('/content/survey.txt')

a

a.shape

"""detractors->0 to 6
passives->7,8
promoters->9,10
"""

detractor=a[a<=6]
detractor.size
a

a>=9
a

promoters=a[a>=9]
promoters.size

"""nps score=%promoters-%detractors

"""

total=a.size
total

nps=(promoters.size/total)*100-(detractor.size/total)*100

nps

"""passives"""

(a>=7) &(a<=8)

paasive=a[(a>=7) &(a<=8)]
paasive.size

detractor.size+paasive+promoters.size==total

"""extreme value for nps"""

nps_mi=0/total*100-total/total*100
nps_mi

nps_max=total/total*100-0/total*100
nps_max

