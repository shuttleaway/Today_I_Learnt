#Find network graph
import numpy as np
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import re

threshold=1

file_loc=r"Posts.xlsx"
xls = pd.ExcelFile(file_loc)
# Now you can list all sheets in the file
temp_names=xls.sheet_names
df_twitter={}
dict={}
overall_dict={}

for names in temp_names:
    df_twitter=pd.read_excel(file_loc,sheetname=names)
    df_twitter=df_twitter.fillna('NaN')
    for j in df_twitter["Names"]:
        if j !='NaN':
            j=j.encode("ascii")
            j=j.replace("[u'","").replace("']","")
            j=j.split("', u'")
            for k in j:
                if dict.has_key(k):
                    dict[k] += 1
                else:
                    dict[k]=1
    overall_dict[names]=dict
    dict={}

#pprint(overall_dict)

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for i in overall_dict.keys():
    for k in overall_dict[i].keys():
        if overall_dict[i][k]>0:
            G.add_edge(i[1:],k,weight=overall_dict[i][k])

#nx.draw(G, with_labels=True, font_weight='normal',node_color='red',node_size=10,width=3)

elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >threshold]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=threshold]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=10)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=3)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=3,alpha=0.5,edge_color='b',style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

plt.show()