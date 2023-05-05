# encoding=utf-8
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import pylab as pl
import  pandas as pd

#domain label:
#Society 0 International 1 Sports 2 Technology 3 Entertainment 4 Finance 5 Military 6

def paint_sankey_domain_patterns():
	#0. read sorted cross-domain patterns data
	df=pd.read_csv("formaldata/mainp_names.csv",encoding='utf-8')

	#1. construct nodes
	nodes=[]
	for i in range(2):
		vales=df.iloc[:,i].unique()
		for value in vales:
			dic={}
			dic['name']=value
			nodes.append(dic)
	print(nodes)

	#2. define edges and flow
	linkes=[]
	for i in df.values:
		dic={}
		dic['source']=i[0]
		dic['target']=i[1]
		dic['value']=i[2]
		linkes.append(dic)
	print(linkes)

	#3. draw Sankey figure
	from pyecharts.charts import Sankey
	from pyecharts import options as opts
	pic=(
		Sankey().add('',
			nodes,
			linkes,
			linestyle_opt=opts.LineStyleOpts(opacity=0.3,curve=0.5,color='source'),
			label_opts=opts.LabelOpts(position='top'),
			node_gap=30,
		).set_global_opts(title_opts=opts.TitleOpts(title='')) #Cross-domain patterns
	)
	pic.render('Across-domain.html')

	from snapshot_phantomjs import snapshot
	from pyecharts.render import make_snapshot
	make_snapshot(snapshot,"Across-domain.html","Across-domain.pdf")

def main():
	paint_sankey_domain_patterns()

if __name__=='__main__':
	main()
