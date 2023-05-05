# encoding=utf-8
import numpy as np
import random
import math
import pandas as pd


#domain label:
#Society 0 International 1 Sports 2 Technology 3 Entertainment 4 Finance 5 Military 6

def sub_ols_relation_of_cross_influence(topic_id,subfig_id,fout):  #Ols for each domains
	print('Ols topic=',topic_id)
	df=pd.read_csv('formaldata/dflg_topic='+str(topic_id)+'.csv')

	import statsmodels.api as sm 
	fout.write('**************************************topic=%s**************************************\n' % (str(topic_id)))
	Y=df['lg(Indegree rank)']
	X=sm.add_constant(df[['Cross-domain capability','lg(Activity)','lg(Followers)','V-1','V0','V1','V2','V3','male','female']]) 
	model=sm.OLS(Y,X).fit()
	print(model.summary())
	fout.write('%s\n' % model.summary())
	fout.write('%s\n' % model.params)
	print(model.params)
	fout.write('**************************************topic=%s**************************************\n' % (str(topic_id)))

def sum_ols_relation_of_cross_influence(): #Ols for all domains
	order_list=[0,1,2,3,4,5,6,'all']
	fout=open('out/Ydegreeranklg_ols.txt','w',encoding='utf-8')
	for (topic_id,subfig_id) in zip(order_list,range(1,2*4+1)):
		sub_ols_relation_of_cross_influence(topic_id,subfig_id,fout)
	fout.close()

def main():
	sum_ols_relation_of_cross_influence() #Ols for all domains

if __name__=='__main__':
	main()
