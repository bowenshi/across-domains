# encoding=utf-8
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import pylab as pl
import itertools

#domain label:
#Society 0 International 1 Sports 2 Technology 3 Entertainment 4 Finance 5 Military 6

def statistic_matrix_vtype(): #statistic cross-domain matrix of each user verified type into dict M(domain1 domain2 vtype_id)
	#1. create matrix M
	xy_m={} #store the number of people with different verified types in cross-domain patterns
	for i in range(0,6):
		xy_m[i]={}
		for j in range(i+1,7):
			xy_m[i][j]={}
			for k in range(-1,4):
				xy_m[i][j][k]=0
	print(xy_m)

	#2. statistic cross-domain matrix
	with open('formaldata/cross_details.txt','r',encoding='utf-8') as fin:
		for line in fin:
			line_arr=line.strip().split('\t')
			vtype=int(line_arr[1])
			if vtype not in range(-1,4):
				continue
			cplist=list(line_arr[2].replace('[','').replace(']','').replace(',','').replace(' ',''))  #cplist:cross-domain pattern list
			if len(cplist)>1:
				for x in range(len(cplist)-1):
					for y in range(x+1,len(cplist)):
						xy_m[int(cplist[x])][int(cplist[y])][vtype]+=1

	#3. output
	with open('xy_m.txt','w') as fout:
		for i in range(0,6):
			for j in range(i+1,7):
				fout.write('%d %d\t%s\n' % (i,j,xy_m[i][j]))
		fout.write('%s' % xy_m)

def sub_paint_xynum_matrix_elite(vtype_id,subfig_id): #paint cross-domain matrix for users of one verified type
	xy_m={0: {0:{0: 116, 1: 7, 2: 4, 3: 44, -1: 28},1: {0: 21, 1: 2, 2: 0, 3: 20, -1: 2}, 2: {0: 13, 1: 0, 2: 0, 3: 6, -1: 3}, 3: {0: 21, 1: 2, 2: 1, 3: 10, -1: 5}, 4: {0: 56, 1: 1, 2: 1, 3: 10, -1: 12}, 5: {0: 16, 1: 3, 2: 1, 3: 24, -1: 4}, 6: {0: 16, 1: 3, 2: 0, 3: 18, -1: 2}}, 1: {1:{0: 61, 1: 11, 2: 8, 3: 55, -1: 59},2: {0: 9, 1: 0, 2: 1, 3: 6, -1: 1}, 3: {0: 12, 1: 2, 2: 3, 3: 11, -1: 4}, 4: {0: 16, 1: 1, 2: 0, 3: 7, -1: 2}, 5: {0: 10, 1: 5, 2: 2, 3: 29, -1: 5}, 6: {0: 17, 1: 4, 2: 2, 3: 28, -1: 16}}, 2: {2:{0: 61, 1: 0, 2: 19, 3: 51, -1: 33},3: {0: 8, 1: 0, 2: 4, 3: 7, -1: 2}, 4: {0: 15, 1: 0, 2: 1, 3: 4, -1: 4}, 5: {0: 6, 1: 0, 2: 1, 3: 6, -1: 1}, 6: {0: 9, 1: 0, 2: 2, 3: 7, -1: 1}}, 3: {3:{0: 82, 1: 2, 2: 66, 3: 23, -1: 23},4: {0: 27, 1: 1, 2: 1, 3: 6, -1: 6}, 5: {0: 16, 1: 2, 2: 3, 3: 15, -1: 1}, 6: {0: 10, 1: 2, 2: 3, 3: 9, -1: 2}},4: {4:{0: 123, 1: 1, 2: 7, 3: 29, -1: 34},5: {0: 15, 1: 1, 2: 0, 3: 6, -1: 2}, 6: {0: 13, 1: 1, 2: 2, 3: 5, -1: 2}},5: {5:{0: 72, 1: 13, 2: 17, 3: 64, -1: 26},6: {0: 8, 1: 4, 2: 2, 3: 21, -1: 5}},6:{6:{0: 80, 1: 12, 2: 9, 3: 41, -1: 50}}}	
	arrayall=np.zeros((7,7),dtype=np.int)
	if vtype_id=='all':
		for i in range(0,7):
			for j in range(0,7):
				if i<j:
					arrayall[i][j]=int(xy_m[i][j][-1]+xy_m[i][j][0]+xy_m[i][j][1]+xy_m[i][j][2]+xy_m[i][j][3])
				elif i==j:
					arrayall[i][j]=0 #int(xy_m[i][j][-1]+xy_m[i][j][0]+xy_m[i][j][1]+xy_m[i][j][2]+xy_m[i][j][3]) #or 0
				else:
					arrayall[i][j]=int(xy_m[j][i][-1]+xy_m[j][i][0]+xy_m[j][i][1]+xy_m[j][i][2]+xy_m[j][i][3])
	else:
		for i in range(0,7):
			for j in range(0,7):
				if i<j:
					arrayall[i][j]=int(xy_m[i][j][vtype_id])
				elif i==j:
					arrayall[i][j]=0 #int(xy_m[j][i][vtype_id]) #or 0
				else:
					arrayall[i][j]=int(xy_m[j][i][vtype_id])
	print('print vtype=',vtype_id)
	title_dict={-1:'Ordinary',0:'Celebrity',1:'Government',2:'Enterprise',3:'Media','all':'All'}
	class_names=['Society','International','Sports','Technology','Entertainment','Finance','Military'] 
	ax = plt.subplot(2,3,subfig_id) #plt.subplots(figsize=(6,5))
	ax.imshow(arrayall, interpolation='nearest', cmap=plt.cm.Blues)

	for i in range(len(class_names)):
		for j in range(len(class_names)):
			text = ax.text(j, i, format(arrayall[i][j],'d'),ha="center", va="center", color="w") #.0f
	if subfig_id in [4,5,6]:
		ax.set_xticks(np.arange(len(class_names)))
		ax.set_xticklabels(class_names,fontsize=8)
		plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor",fontsize=10)
	else:
		ax.set_xticks(np.arange(len(class_names)))
		ax.set_xticklabels([])
		plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")

	if subfig_id in [1,4]:
		ax.set_yticks(np.arange(len(class_names)))
		ax.set_yticklabels(class_names,fontsize=10)
	else:
		ax.set_yticks(np.arange(len(class_names)))
		ax.set_yticklabels([])
	#if subfig_id in [1,5]:
	#	plt.ylabel('Probability of \nhomophily retweeting') #Proportion probability density function CDF（cumulative distribution function）
	plt.title(title_dict[vtype_id],fontsize=15) #,fontsize = 15)

def sum_paint_xynum_matrix(): #paint cross-domain matrix for various users
	#plt.figure(figsize=(12,8))  #7.68,13.66
	fig,axes=plt.subplots(nrows=2,ncols=3,figsize=(10.09, 14.47)) 
	plt.subplots_adjust(wspace = 0.1,hspace=0.1) #plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=None)
	order_list=['all',-1,0,1,2,3]
	for (vtype_id,subfig_id) in zip(order_list,range(1,2*3+1)):
		#print topic_id,type(topic_id)
		#ax.yaxis.grid(True)
		#print subfig_id
		#sub_paint_homophily_matrix(topic_id,subfig_id)
		sub_paint_xynum_matrix_elite(vtype_id,subfig_id)
	plt.savefig('rq.pdf',format='pdf',dpi=300,bbox_inches = 'tight')
	plt.savefig('rq.png',format='png',dpi=300,bbox_inches = 'tight')
	plt.show()

def main():
	#statistic_matrix_vtype() #statistic cross-domain matrix of each user verified type into dict M(domain1 domain2 vtype_id)
	sum_paint_xynum_matrix()  #paint cross-domain matrix for various users

if __name__=='__main__':
	main()
