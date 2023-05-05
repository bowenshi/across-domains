# encoding=utf-8
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns
import pandas as pd

#domain label:
#Society 0 International 1 Sports 2 Technology 3 Entertainment 4 Finance 5 Military 6

def sub_paint_specialist_generalist_vinlion(topic_id,subfig_id): #paint for each domain
	print('paint vinlion of topic=',topic_id)
	df=pd.read_csv('formaldata/dflg_topic='+str(topic_id)+'.csv')
	arr1= df[df['Group']=='Specialist']['Indegree ranklg']
	arr2= df[df['Group']=='Generalist']['Indegree ranklg']

	plt.subplot(2,4,subfig_id)
	da,tou,lwsize=10,0.7,4.5
	x = [1, 2, 3, 4, 5, 6 ,7,8,9,10]
	title_dict={0:'Society',1:'International',2:'Sports',3:'Technology',4:'Entertainment',5:'Finance',6:'Military','all':'All'}
	sns.set(style="white", palette="pastel", color_codes=True)
	sns.violinplot(x="Group", y="Indegree ranklg",split=True, order=["Specialist", "Generalist"], inner="quart",palette={ "Specialist": "r","Generalist": "b"},data=df) #, hue="group" split

	#plt.xlabel("Ranking of opinion leaders")
	plt.xlabel('')
	plt.ylabel('')
	#plt.yscale('log')
	#plt.ylabel("Proportion")
	#plt.ylim(0,1)
	#plt.legend()
	plt.title(title_dict[topic_id],fontsize=12)
	#if subfig_id in xrange(5,9): 
	#	plt.xlabel('Ranking of opinion leaders',fontsize=12)
	if subfig_id in [1,5]:
		plt.ylabel('lg(Indegree rank)',fontsize=12)
	#plt.show()

def sum_paint_specialist_generalist_vinlion(): #paint for all domains
	#plt.figure(figsize=(12,8))
	fig,axes=plt.subplots(nrows=2,ncols=4,figsize=(19.2,10.8))  #13.66,7.68  14.2,8   1920×1080
	plt.subplots_adjust(wspace = 0.2,hspace=0.2) #plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=None)
	order_list=[0,1,2,3,4,5,6,'all']
	for (topic_id,subfig_id) in zip(order_list,range(1,2*4+1)):
		#ax.yaxis.grid(True)
		sub_paint_specialist_generalist_vinlion(topic_id,subfig_id)
	plt.savefig('h1b_indegreeranklg.pdf',format='pdf',dpi=300,bbox_inches = 'tight')   
	plt.savefig('h1b_indegreeranklg.png',format='png',dpi=300,bbox_inches = 'tight')
	plt.show()

def main():
	#sub_paint_specialist_generalist_vinlion(0,1) #paint for each domain
	sum_paint_specialist_generalist_vinlion() #paint for all domains

if __name__=='__main__':
	main()
