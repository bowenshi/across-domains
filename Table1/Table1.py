# encoding=utf-8
import numpy as np
import random
import math
import statsmodels.stats.weightstats as sw
import pandas as pd

#domain label:
#Society 0 International 1 Sports 2 Technology 3 Entertainment 4 Finance 5 Military 6

def sub_specialist_generalist_ztest(topic_id,subfig_id,fout): #Ztest for each domain
	print('Ztest topic=',topic_id)
	df=pd.read_csv('formaldata/df_topic='+str(topic_id)+'.csv')
	arr1= df[df['Group']=='Specialist']['Indegree rank']
	arr2= df[df['Group']=='Generalist']['Indegree rank']
	ztest= sw.ztest(arr1, arr2, value=0)
	fout.write('topic=%s\t%s\n' % (str(topic_id),ztest))

def sum_specialist_generalist_ztest(): #Ztest for all domains
	order_list=[0,1,2,3,4,5,6,'all']
	fout=open('out/indegreerank_ztest.txt','w',encoding='utf-8') 
	for (topic_id,subfig_id) in zip(order_list,range(1,2*4+1)):
		sub_specialist_generalist_ztest(topic_id,subfig_id,fout)
	fout.close()

def main():
	sum_specialist_generalist_ztest() #Ztest for all domains

if __name__=='__main__':
	main()
