import sys,os
import numpy as np
from scipy.linalg import qr
from random import gauss

def orthogonal_gen(k):
	H = np.random.randn(k, k)
	Q, R = qr(H)	
	return Q

def random_matrix_t(k):
	t = np.random.rand(k,1)
	return t

def gaussian_matrix(k,sig):
	values = []
	while len(values) < k:
		lst = []
		while True:
    			value = gauss(0, sig)
    			if 0 < value < sig:
				lst.append(value)
        			values.append(lst)
				break
	return np.array(values)


def readSVM(fn):
	labels = []
	records = []
	f = open(fn)
	ncols = 0
	for line in f.readlines():
		fields = line.strip().split(" ")
		labels.append(int(fields[0])) #assume labels are integers
		r = {}
		for v in fields[1:]:
			i, u = v.split(":")
			i = int(i)
			r[i] = float(u)
			if i> ncols:
				ncols = i
		records.append(r)

	records2=[]
	for r in records:
		v = [0]*ncols # if the field is not mentioned, the default value is 0
		for i in r:
			# the field id starts from 1
			v[i-1] =r[i]
		records2.append(v)

	return labels, records2

if __name__ == '__main__':
	lab,rec = readSVM(sys.argv[2])
	o = orthogonal_gen(len(rec[0]))
	t = random_matrix_t(len(rec[0]))
	
		
	
	iter = 0
	fw = open(sys.argv[3],"w")
	

	for val in rec:
		lst = []
		for i in val:
			temp = []
			temp.append(i)
			lst.append(temp)
		x =  np.array(lst)

		Rx = o.dot(x)
		d = gaussian_matrix(len(val),float(sys.argv[1]))
		
		y = np.add(Rx,t,d)
		y = y.T
		y = y[0]
		
		fw.write(str(lab[iter]))
		#print lab[iter],

		for j in range(0,len(y)):
			fw.write(" "  + str(j+1) + ":" + str(round(y[j],6)))	
			#print " "  + str(j+1) + ":" + str(round(y[j],6)),
		fw.write("\n")
		#print "\n" 
		iter = iter + 1
	#print iter
	fw.close()
		#print y
		
		#print x
		#print "##################################################"
	#print y_con

	
	
	
	
