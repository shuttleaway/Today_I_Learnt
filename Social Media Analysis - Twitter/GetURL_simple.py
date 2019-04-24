#Extract URL and find best sources
import pandas as pd

file_loc=r"Posts.xlsx"
xls = pd.ExcelFile(file_loc)
# Now you can list all sheets in the file
temp_names=xls.sheet_names
df_twitter={}
url=[]
url_long=[]

for names in temp_names:
    df_twitter=pd.read_excel(file_loc,sheetname=names)
    df_twitter=df_twitter.fillna('')
    for j in df_twitter["URL"]:
        #print j
        if j !="": 
            url_long.append(j)
            url.append(j.split("//")[-1].split("/")[0])

count_url={}
for i in url:
   count_url[i]=url.count(i)

for key, value in sorted(count_url.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    print "%s: %s" % (key, value)