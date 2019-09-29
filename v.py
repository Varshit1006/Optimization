from sympy import * 
import numpy as np

x = symbols('x')

Q = lambda x: np.array([[2,x,x],[0,4,0],[x,x,6]])
P =  np.array([[1,1,1],[0,2,2],[0,0,3]])
R = lambda x: np.matmul((np.matmul(P,Q)),np.linalg.inv(P))

#option 1 solution
#Find does there exists a real number x such that PQ=QP
PQ = lambda x: np.matmul(P,Q)
QP = lambda x: np.matmul(Q,P)


if (PQ == QP):
	print('There exists a real x - option 1 correct')
else :
	print('There doesnot exist a real x - option 1 wrong')

#option 2 solution 
#Show det(R)=48-4x^2

S = lambda x: np.array([[2,x,x],[0,4,0],[x,x,5]])
k = lambda x: np.linalg.det((S(x))) + 8

if (k == np.linalg.det(R(x))):
	print('Equal - option 2 correct')
else :
	print('Not Equal - option 2 wrong')
	
#option 3 solution
# Find a+b

w,v = np.linalg.eig(R(0))
a = V[1][2]
b = V[2][2]

print("a + b = " , end = " ")
print(a + b)
#option 4 solution
#find if there exists a unit vector αi + βj + γk , such that it satisfies given condition

O = np.array([0,0,0])
C = np.matmul(O,np.linalg.inv(R))

if (np.linalg.det(R(x) != 0):
	print('There doesnot exist such a unit vector - option 4 wrong')
else :
	print('There exists such a unit vector - option 4 correct')

