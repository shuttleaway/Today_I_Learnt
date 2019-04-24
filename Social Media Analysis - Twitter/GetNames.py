#GetNames
#Find @...
#ValueError: If using all scalar values, you must pass an index

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
    if pd.DataFrame(df_twitter).empty==False:
        #print(pd.DataFrame(df_twitter).empty)
        for j in df_twitter["Names"]:
            if j !='NaN':
                j=j.encode("ascii")
                j=j.replace("[u'","").replace("']","").lower()
                j=j.split("', u'")
                for k in j:
                    if dict.has_key(k):
                        dict[k] += 1
                    else:
                        dict[k]=1
        overall_dict[names]=dict
        #dict={}

#pprint(overall_dict)
#pprint(dict)

for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    print "%s: %s" % (key, value)

#df_twitter = pd.DataFrame.from_records(data = dict)
df_twitter = pd.DataFrame({"key": dict.keys(), "value": dict.values()})
df_twitter=df_twitter.sort_values(by= "value", ascending=False)
df_twitter.to_csv("NewExpertNames.csv",index=False,header=True)