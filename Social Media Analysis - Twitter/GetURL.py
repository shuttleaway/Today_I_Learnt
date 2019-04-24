#Extract URL and find best sources
#IOError: [Errno socket error] [Errno 11002] getaddrinfo failed

import pandas as pd
from pprint import pprint
import requests
import urllib

def unshorten_url(url):
    resp = urllib.urlopen(url)
    return resp.url

file_loc=r"Posts.xlsx"
xls = pd.ExcelFile(file_loc)
# Now you can list all sheets in the file
temp_names=xls.sheet_names
df_twitter={}
url=[]
url_long=[]
pprint(temp_names)
for names in temp_names:
    print names
    df_twitter=pd.read_excel(file_loc,sheetname=names)
    df_twitter=df_twitter.fillna('')
    for j in df_twitter["URL"]:
        #print j
        if j !="": 
            if len(j)<23:
                temp_url=unshorten_url(j)
            else:
                temp_url=j
            url_long.append(temp_url)
            url.append(temp_url.split("//")[-1].split("/")[0])
            j=temp_url

pprint(url_long)
count_url={}
for i in url:
   count_url[i]=url.count(i)

for key, value in sorted(count_url.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    print "%s: %s" % (key, value)