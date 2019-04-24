import random
import string
import time


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

def min_inv2(perm, dic=dict()) :
	if nb_adjacences(perm)==len(perm)+1 :
		dic[perm]=0
		return 0
	else :
		perm1=permut_1_inv(perm)
		if perm1 :
			nb_min=[]
			for p in perm1 :
				if p in dic :
					nb_min.append(dic[p])
				else :
					nb_min.append(min_inv2(p, dic))
			dic[perm]=min(nb_min)+1
			return min(nb_min)+1
		dic[perm]=float("inf")
		return float("inf")

def echantillon(n) :
	ascii=string.ascii_uppercase[:n]
	a=''
	for _ in range(n) :
		c=random.choice(ascii)
		ascii=ascii.replace(c,'')
		a+=c
	return a

if __name__=="__main__" :
#test pour le temps d'exécution de la fonction de distance optimisée, permutations de longueur 6 à 13 (à 13 on a environ 6min)
	"""for i in range(6,14) :
		print "test min_inv2 a %d" % i
		start_time=time.time()
		perm=echantillon(i)
		print "min_inv2 : " +str(min_inv2(perm))
		print "temps d'exe : %s sec" % (time.time()-start_time)
		print"""
	
	
	l=[]
	t=[]
	b=0
	
	
#calcul de la distance d'inversion pour 20 permutations de taille 13 ; affiche à chaque fois : le numéro d'itération, le temps de calcul de la i-ème itération, le temps moyen de calcul des i premières itérations, la distance de la i-ème permutation, la distance moyenne des i premières, la proportion de pemutation de distance <=7 parmi les i premières itérations
	print('iter\ttemps\ttps moy\tdist\td moy\tp-val')
	for _ in range(20) :
		start_time=time.time()
		d=min_inv2(echantillon(13))
		t.append(time.time()-start_time)
		if d!=float('inf') :
			l.append(d)
			if d<=7 :
				b+=1
		print(str(_)+'\t'+str(t[_])+'\t'+str(sum(t)/len(t))+'\t'+str(d)+'\t'+str(sum(l)/float(len(l)))+'\t'+str(float(b)/float(len(l))))
	print
#distance moyenne d'inversion
	print float(sum(l))/float(len(l))
#proportion de permutations de distance <=7 (pvalue du test)
	print float(b)/float(len(l))
