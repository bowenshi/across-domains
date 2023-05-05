# encoding=utf-8
import numpy as np
import random
import math

#domain label:
#Society 0 International 1 Sports 2 Technology 3 Entertainment 4 Finance 5 Military 6

def read_crossdetails_sortpatterns(): #Read details of elite's cross-domain attribute, count, sort and output  cross domain patterns by their frequencies
	cpdic={} #cross patterns dict
	cpndic={} #store the cross num of each pattern

	print('0. begin to read the cross num of 990 elites')
	with open('formaldata/cross_details.txt','r') as fin: #度跨界数目等 info
		for line in fin:
			line_arr=line.strip().split('\t')
			cp=line_arr[2]
			if cp in cpdic:
				cpdic[cp]+=1
			else:
				cpdic[cp]=1
				cplist=cp.strip().split(',')
				#print cplist
				cpndic[cp]=len(cplist)
	with open('sorted_cross_patterns.txt','w') as fout:
		for item in sorted(cpdic.items(),key=lambda asd:asd[1],reverse=True):
			fout.write('%s\t%d\t%d\n' % (item[0],item[1],cpndic[item[0]]))

def main():
	read_crossdetails_sortpatterns() #Read details of elite's cross-domain attribute, count, sort and output  cross domain patterns by their frequencies

if __name__=='__main__':
	main()
