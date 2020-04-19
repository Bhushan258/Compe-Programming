from itertools import permutations

def ispallin(L):
	if len(L)==0:
		return False
	else:
		if L==L[::-1]:
			return True
		else:
			temp=permutations(L)
			for i in list(temp):
				if i ==i[::-1]:
					return True
			return False
Q=int(input())
S=str(input())
while (Q!=0) :
	a=input()
	b=a.split()
	Li=list(int(i) for i in b)
	Li[0]-=1
	Lo=S[Li[0]:Li[1]]
	Res=ispallin(Lo)
	if Res is True:
		print("Possible")
	else:
		print("Impossible")
	Q-=1
