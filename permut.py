import random
import string

def nb_adjacences(permutation) :
	a=0
	for i in range(len(permutation)-1) :
		if ord(permutation[i+1])==ord(permutation[i])+1 or ord(permutation[i+1])==ord(permutation[i])-1 :
			a+=1
	if permutation[0]==min(permutation) :
		a+=1
	if permutation[len(permutation)-1]==max(permutation) :
		a+=1
	return a

def permut_1_inv(permutation) :
	inv=list()
	nb=nb_adjacences(permutation)
	for i in range(len(permutation)-1) :
		for j in range(i+1,len(permutation)) :
			p=permutation[:i]+permutation[i:j+1][::-1]+permutation[j+1:]
			if nb_adjacences(p)>nb :
				inv.append(p)
	return inv

def min_inv(perm, nb=0) :
	if nb_adjacences(perm)==len(perm)+1 :
		return nb
	else :
		perm1=permut_1_inv(perm)
		if perm1 :
			nb_min=[]
			for p in perm1 :
				nb_min.append(min_inv(p,nb+1))
			return min(nb_min)
		return(float("inf"))

def echantillon(n) :
	ascii=string.ascii_uppercase[:n]
	a=''
	for _ in range(n) :
		c=random.choice(ascii)
		ascii=ascii.replace(c,'')
		a+=c
	return a

if __name__=="__main__" :
	l=[]
	for __ in range(10) :
		for _ in range(100) :
			r=min_inv(echantillon(7))
			if r!=float('inf') :
				l.append(r)
		print float(sum(l))/float(len(l))
