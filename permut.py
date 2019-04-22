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
	
if __name__=="__main__" :
	permut="ABCD"
	print(nb_adjacences(permut))
